from __future__ import annotations
import json, math, time, urllib.request, urllib.error

def l2_normalize(vec: list[float]) -> list[float]:
    norm = math.sqrt(sum(x*x for x in vec)) or 1.0
    return [x / norm for x in vec]

def require_equal_length(left_name: str, left, right_name: str, right, context: str):
    if len(left) != len(right):
        raise RuntimeError(
            f'{context}: {left_name} count {len(left)} != {right_name} count {len(right)}. '
            'Refuse to continue because zip() would silently drop rows.'
        )

def require_vector_dimensions(
    vectors: list[list[float]],
    context: str,
    expected_dim: int | None = None,
) -> int:
    if not vectors:
        return expected_dim or 0
    first = vectors[0]
    if not isinstance(first, list) or not first:
        raise RuntimeError(f'{context}: first vector is missing or empty.')
    dim = len(first)
    if expected_dim is not None and dim != expected_dim:
        raise RuntimeError(f'{context}: vector dim {dim} != expected dim {expected_dim}.')
    for i, vec in enumerate(vectors, 1):
        if not isinstance(vec, list) or not vec:
            raise RuntimeError(f'{context}: vector #{i} is missing or empty.')
        if len(vec) != dim:
            raise RuntimeError(f'{context}: vector #{i} dim {len(vec)} != expected batch dim {dim}.')
        if expected_dim is not None and len(vec) != expected_dim:
            raise RuntimeError(f'{context}: vector #{i} dim {len(vec)} != expected dim {expected_dim}.')
    return dim

def embed_lmstudio(
    texts: list[str],
    endpoint: str = 'http://localhost:1234/v1/embeddings',
    model: str = 'bge-small-en-v1.5',
    batch_size: int = 16,
    normalize: bool = True,
) -> list[list[float]]:
    vectors: list[list[float]] = []
    expected_dim: int | None = None
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        payload = {'model': model, 'input': batch}
        data = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(endpoint, data=data, headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                obj = json.loads(r.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            detail = e.read().decode('utf-8', 'ignore')
            raise RuntimeError(f'Embedding HTTP {e.code}: {detail}') from e
        except Exception as e:
            raise RuntimeError(f'Failed to call embedding endpoint {endpoint}: {e}') from e
        raw_items = obj.get('data')
        context = f'embed_lmstudio batch {i//batch_size + 1} ({len(batch)} texts)'
        if not isinstance(raw_items, list):
            raise RuntimeError(f'{context}: embedding response is missing a valid `data` list.')
        if len(raw_items) != len(batch):
            raise RuntimeError(
                f'{context}: endpoint returned {len(raw_items)} vectors for {len(batch)} texts. '
                'Refuse to continue because later zip() calls would silently drop rows.'
            )
        items = sorted(raw_items, key=lambda x: x.get('index', -1))
        indexes = [item.get('index') for item in items]
        expected_indexes = list(range(len(batch)))
        if indexes != expected_indexes:
            raise RuntimeError(
                f'{context}: endpoint returned indexes {indexes}, expected {expected_indexes}.'
            )
        for item in items:
            embedding = item.get('embedding')
            if not isinstance(embedding, list) or not embedding:
                raise RuntimeError(f'{context}: embedding payload is missing or empty.')
            try:
                v = [float(x) for x in embedding]
            except Exception as e:
                raise RuntimeError(f'{context}: embedding payload contains non-numeric values.') from e
            if expected_dim is None:
                expected_dim = len(v)
            elif len(v) != expected_dim:
                raise RuntimeError(
                    f'{context}: embedding dim {len(v)} != expected dim {expected_dim}.'
                )
            vectors.append(l2_normalize(v) if normalize else v)
        print(f'embedded {min(i+batch_size, len(texts))}/{len(texts)}')
        time.sleep(0.02)
    require_equal_length('texts', texts, 'vectors', vectors, 'embed_lmstudio')
    require_vector_dimensions(vectors, 'embed_lmstudio', expected_dim=expected_dim)
    return vectors

def dot(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise RuntimeError(f'dot: vector dim mismatch {len(a)} != {len(b)}.')
    return sum(x*y for x,y in zip(a,b))

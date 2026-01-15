import re
from typing import Set, List, Iterable

SPECIAL_TOKENS = {
    "c++":"cpp",
    "c#":"csharp",
    ".net":"dotnet"
}

STOPWORDS = {
    "a", "an", "and", "or", "the", "to", "of", "in", "for", "with", "on", "at", "by", "from",
    "as", "is", "are", "be", "will", "may", "must",
    "ability", "able", "strong", "excellent", "good", "proven", "demonstrated",
    "experience", "years", "year", "plus", "required", "preferred", "skills", "skill",
    "knowledge", "familiarity", "understanding", "hands", "hands-on",
    "develop", "developing", "development", "build", "building", "implement", "implementation",
}

CANONICAL_PHRASES = [
    (r"\bci\s*[/\-]\s*cd\b", "ci_cd"),
    (r"\bcontinuous\s+integration\b", "ci_cd"),
    (r"\bcontinuous\s+delivery\b", "ci_cd"),
    (r"\brestful\b", "rest"),
    (r"\brest\s+api(s)?\b", "rest_api"),
    (r"\bapi\s+design\b", "api_design"),
    (r"\bmachine\s+learning\b", "machine_learning"),
    (r"\bml\b", "machine_learning"),
    (r"\blarge\s+language\s+model(s)?\b", "llm"),
    (r"\bllm(s)?\b", "llm"),
    (r"\bretrieval\s*[- ]\s*augmented\s*[- ]\s*generation\b", "rag"),
    (r"\brag\b", "rag"),
    (r"\bvector\s+db\b", "vector_database"),
    (r"\bvector\s+database\b", "vector_database"),
    (r"\bnode\.?js\b", "nodejs"),
    (r"\breact\.?js\b", "react"),
    (r"\bpostgre\s*sql\b", "postgresql"),
    (r"\baws\b", "aws"),
    (r"\bazure\b", "azure"),
]

def _normalise_text(text: str) -> str:
    text = text.lower().strip()

    for key, val in SPECIAL_TOKENS.items():
        text = text.replace(key, val)
    
    for pattern, repl in CANONICAL_PHRASES:
        text = re.sub(pattern, repl, text)
    
    text = text.replace("&", " and ")
    text = re.sub(r"[/\-]", " ", text)

    text = re.sub(r"[^a-z0-9_\s]", " ", text)
    
    text = re.sub(r"\s+", " ", text).strip()
    return text

def _tokens(text: str) -> List[str]:
    return [t for t in text.split(" ") if t]

def _remove_stopwords(tokens: Iterable[str]) -> List[str]:
    return [t for t in tokens if t not in STOPWORDS]

def _light_lemmatise(tokens: Iterable[str]) -> List[str]:
    out = []
    for t in tokens:
        if len(t) > 4 and t.endswith("ies"):
            t = t[:-3] + "y"
        elif len(t) > 3 and t.endswith("s") and not t.endswith("ss"):
            t = t[:-1]

        for suf in ("ing", "ed"):
            if len(t) > 5 and t.endswith(suf):
                t = t[: -len(suf)]
                break
        out.append(t)
    return out

def _add_ngrams(tokens: list[str], n: int) -> Set[str]:
    return {"_".join(tokens[i : i + n]) for i in range(len(tokens) - n + 1)} if len(tokens) >= n else set()

def text_normalisation(text: str) -> Set[str]:
    """Normalisation pipeline.

    Args:
        text (str): Input string of text.
    
    Returns:
        Set[str]: Set of canonical tokens.
    """

    text = _normalise_text(text)
    toks = _tokens(text)
    toks = _remove_stopwords(toks)
    toks = _light_lemmatise(toks)

    token_set = set(toks)

    # include n-grams so multi-word skills match
    token_set |= _add_ngrams(toks, 2)
    token_set |= _add_ngrams(toks, 3)

    return token_set

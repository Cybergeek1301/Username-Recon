import json
from username_recon.providers import github

class DummyResp:
    def __init__(self, status_code=200):
        self.status_code = status_code


def test_github_provider_found(monkeypatch):
    def fake_head(url, timeout, allow_redirects):
        return DummyResp(status_code=200)
    monkeypatch.setattr(github.requests, "head", fake_head)
    res = github.check("someuser")
    assert res["service"] == "github"
    assert res["found"] is True


def test_github_provider_not_found(monkeypatch):
    def fake_head(url, timeout, allow_redirects):
        return DummyResp(status_code=404)
    monkeypatch.setattr(github.requests, "head", fake_head)
    res = github.check("nouser")
    assert res["found"] is False

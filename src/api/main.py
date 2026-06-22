"""FastAPI application — health and metrics stubs for the portfolio template."""

from fastapi import FastAPI, Response

app = FastAPI(
    title="Cyber AI Project Template",
    description="Portfolio template API — extend with agent routes per project.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe for Docker and load balancers."""
    return {"status": "ok"}


@app.get("/metrics")
def metrics() -> Response:
    """Prometheus-style metrics stub — extend with counters and histograms per project."""
    body = "\n".join(
        [
            "# HELP cyber_ai_up Application is running",
            "# TYPE cyber_ai_up gauge",
            "cyber_ai_up 1",
            "# HELP cyber_ai_http_requests_total Total HTTP requests (stub)",
            "# TYPE cyber_ai_http_requests_total counter",
            "cyber_ai_http_requests_total{endpoint=\"health\"} 0",
            "# HELP cyber_ai_agent_invocations_total Agent invocations (stub)",
            "# TYPE cyber_ai_agent_invocations_total counter",
            "cyber_ai_agent_invocations_total 0",
            "",
        ]
    )
    return Response(content=body, media_type="text/plain; version=0.0.4; charset=utf-8")

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Set up tracing
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(
  OTEL_EXPORTER_OTLP_ENDPOINT="https://ingest.<region>.signoz.cloud:443" \ 
OTEL_EXPORTER_OTLP_HEADERS="signoz-ingestion-key=<e2800c85-0d33-4977-b261-91ff8501ca7a>" \

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

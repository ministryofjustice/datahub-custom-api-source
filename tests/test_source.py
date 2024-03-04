from datahub.ingestion.api.common import PipelineContext

from datahub_custom_api_source.config import JusticeDataAPIConfig
from datahub_custom_api_source.source import JusticeDataAPISource


def test_host_port_parsing():
    examples = [
        "http://localhost:8080",
        "localhost",
        "192.168.0.1",
        "https://192.168.0.1/",
    ]

    for example in examples:
        config_dict = {"base_url": example}
        config = JusticeDataAPIConfig.parse_obj(config_dict)
        assert config.base_url == example


def test_ingest():
    source = JusticeDataAPISource(
        ctx=PipelineContext(run_id="justice-api-source-test"),
        config=JusticeDataAPIConfig(base_url="data.justice.gov.uk"),
    )
    assert source.get_workunits() == []

from io import BufferedReader
from typing import Iterable, Optional

from datahub.ingestion.api.common import PipelineContext
from datahub.ingestion.api.decorators import (
    SupportStatus,
    config_class,
    platform_name,
    support_status,
)
from datahub.ingestion.api.source import (
    CapabilityReport,
    SourceReport,
    TestableSource,
    TestConnectionReport,
)
from datahub.ingestion.api.workunit import MetadataWorkUnit

from .config import JusticeDataAPIConfig


@platform_name("File")
@config_class(JusticeDataAPIConfig)
@support_status(SupportStatus.CERTIFIED)
class JusticeDataAPISource(TestableSource):
    """
    This plugin pulls metadata from the Justice Data API
    """

    def __init__(self, ctx: PipelineContext, config: JusticeDataAPIConfig):
        self.ctx = ctx
        self.config = config
        self.report = SourceReport()
        self.fp: Optional[BufferedReader] = None

    @classmethod
    def create(cls, config_dict, ctx):
        config = JusticeDataAPIConfig.parse_obj(config_dict)
        return cls(ctx, config)

    def get_workunits(self) -> Iterable[MetadataWorkUnit]:
        return []

    def get_report(self):
        return self.report

    @staticmethod
    def test_connection(config_dict: dict) -> TestConnectionReport:
        return TestConnectionReport(
            basic_connectivity=CapabilityReport(
                capable=False,
                failure_reason=f"Haven't implemented this yet!",
            )
        )

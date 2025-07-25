import types
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import ClassVar

from pony.orm import dbapiprovider, dbschema
from pony.orm.dbapiprovider import DBAPIProvider, Pool
from pony.orm.sqlbuilding import SQLBuilder, Value
from pony.orm.sqltranslation import SQLTranslator
from psycopg2._psycopg import _Connection

NoneType: type[None]

class PGColumn(dbschema.Column):
    auto_template: ClassVar[str]

class PGSchema(dbschema.DBSchema):
    dialect: ClassVar[str]
    column_class: ClassVar[type[PGColumn]]

class PGTranslator(SQLTranslator):
    dialect: ClassVar[str]

class PGValue(Value): ...

class PGSQLBuilder(SQLBuilder):
    dialect: ClassVar[str]
    value_class: ClassVar[type[PGValue]]
    def INSERT(builder, table_name, columns, values, returning=None): ...
    def TO_INT(builder, expr): ...
    def TO_STR(builder, expr): ...
    def TO_REAL(builder, expr): ...
    def DATE(builder, expr): ...
    def RANDOM(builder): ...
    def DATE_ADD(builder, expr, delta): ...
    def DATE_SUB(builder, expr, delta): ...
    def DATE_DIFF(builder, expr1, expr2): ...
    def DATETIME_ADD(builder, expr, delta): ...
    def DATETIME_SUB(builder, expr, delta): ...
    def DATETIME_DIFF(builder, expr1, expr2): ...
    def eval_json_path(builder, values: Iterable[int | str]) -> str: ...  # type: ignore[override]
    def JSON_QUERY(builder, expr, path): ...
    json_value_type_mapping: dict[type, str]
    def JSON_VALUE(builder, expr, path, type): ...
    def JSON_NONZERO(builder, expr): ...
    def JSON_CONCAT(builder, left, right): ...
    def JSON_CONTAINS(builder, expr, path, key): ...
    def JSON_ARRAY_LENGTH(builder, value): ...
    def GROUP_CONCAT(builder, distinct, expr, sep=None): ...
    def ARRAY_INDEX(builder, col, index): ...
    def ARRAY_CONTAINS(builder, key, not_in, col): ...
    def ARRAY_SUBSET(builder, array1, not_in, array2): ...
    def ARRAY_LENGTH(builder, array): ...
    def ARRAY_SLICE(builder, array, start, stop): ...
    def MAKE_ARRAY(builder, *items): ...

class PGIntConverter(dbapiprovider.IntConverter):
    signed_types: Incomplete
    unsigned_types: Incomplete

class PGRealConverter(dbapiprovider.RealConverter):
    def sql_type(converter): ...

class PGBlobConverter(dbapiprovider.BlobConverter):
    def sql_type(converter): ...

class PGTimedeltaConverter(dbapiprovider.TimedeltaConverter): ...
class PGDatetimeConverter(dbapiprovider.DatetimeConverter): ...

class PGUuidConverter(dbapiprovider.UuidConverter):
    def py2sql(converter, val): ...

class PGJsonConverter(dbapiprovider.JsonConverter):
    def sql_type(self): ...

class PGArrayConverter(dbapiprovider.ArrayConverter):
    array_types: dict[type, tuple[str, type]]

class PGPool(Pool):
    def release(pool, con) -> None: ...

ADMIN_SHUTDOWN: str

class PGProvider(DBAPIProvider):
    dialect: ClassVar[str]
    dbapi_module: ClassVar[types.ModuleType]
    dbschema_cls: ClassVar[type[PGSchema]]
    translator_cls: ClassVar[type[PGTranslator]]
    sqlbuilder_cls: ClassVar[type[PGSQLBuilder]]
    array_converter_cls: ClassVar[type[PGArrayConverter]]
    default_schema_name: ClassVar[str]
    fk_types: ClassVar[dict[str, str]]
    converter_classes: list[tuple[type | tuple[type], type]]
    def normalize_name(provider, name: str) -> str: ...
    def inspect_connection(provider, connection: _Connection) -> None: ...
    def should_reconnect(provider, exc: BaseException | None) -> bool: ...
    def get_pool(provider, *args, **kwargs) -> PGPool: ...
    def set_transaction_mode(provider, connection: _Connection, cache) -> None: ...
    def execute(provider, cursor, sql, arguments=None, returning_id: bool = False): ...
    def table_exists(provider, connection: _Connection, table_name: str, case_sensitive: bool = True): ...
    def index_exists(provider, connection: _Connection, table_name: str, index_name, case_sensitive: bool = True): ...
    def fk_exists(provider, connection: _Connection, table_name: str, fk_name, case_sensitive: bool = True): ...
    def drop_table(provider, connection: _Connection, table_name: str) -> None: ...

provider_cls = PGProvider

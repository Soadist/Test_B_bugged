from russian_fields import INNBusinessField, KPPField, OGRNField


class FixedINNBusinessField(INNBusinessField):
    def from_db_value(self, value, expression, connection, context=None):
        return super().from_db_value(value, expression, connection, context)


class FixedKPPField(KPPField):
    def from_db_value(self, value, expression, connection, context=None):
        return super().from_db_value(value, expression, connection, context)


class FixedOGRNField(OGRNField):
    def from_db_value(self, value, expression, connection, context=None):
        return super().from_db_value(value, expression, connection, context)

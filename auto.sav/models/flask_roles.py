# =============================================================================
# Auto-Generated code. do not modify
# (c) Sertechno 2018
# GLVH @ 2019-08-20 18:43:44
# =============================================================================

class Role(db.Model):
    __tablename__ = 'Roles'
    id          = db.Column( db.Integer, primary_key=True )
    name        = db.Column( db.String(64) )
    default     = db.Column( db.Boolean )
    permissions = db.Column( db.Integer )

    users       = db.relationship('User',backref='role')

    def __init__(self, id=None, name='None', default=None, permissions=None):
        self.id          = id
        self.name        = name
        self.default     = default
        self.permissions = permissions

    def __repr__(self):
        return "<Roles( id='%s', name='%s', default='%s', permissions='%s')>" % \
                ( self.id, self.name, self.default, self.permissions)

    @staticmethod
    def insert_roles():
        roles = {
            'Customer': (   Permission.CUSTOMER, False),
            'Reporter': (   Permission.VIEW |
                            Permission.REPORT |
                            Permission.EXPORT, True),
            'Charger': (    Permission.VIEW |
                            Permission.DELETE |
                            Permission.MODIFY |
                            Permission.REPORT, False),
            'Administrator':    (0xfe, False),                      # Administrator does not have 'Customer' permisions
            'Auditor':          (0x1fe, False),                      # Auditor does not have 'Customer' permissions
            'God':              (0xfff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()
    """
    def __repr__(self):
        return '<Role %r>' % self.name
    """

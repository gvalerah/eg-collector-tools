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

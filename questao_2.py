results = session.query(
    user.name,
    user.email,
    claims.description.label('claims'),
    roles.description.label('role')
).join(user_claims, user.id == user_claims.user_id
).join(claims, claims.id == user_claims.claim_id
).join(roles, roles.id == user.role_id
).all()
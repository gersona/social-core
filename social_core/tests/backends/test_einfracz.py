from .oauth import BaseAuthUrlTestMixin, OAuth2Test
from .test_open_id_connect import OpenIdConnectTestMixin


class EInfraCZOpenIdConnectTest(OpenIdConnectTestMixin, OAuth2Test):
    backend_path = "social_core.backends.einfracz.EInfraCZOpenIdConnect"
    issuer = "https://login.e-infra.cz/oidc/"
    openid_config_body = """
    {
    "request_parameter_supported":true,
    "claims_parameter_supported":false,
    "introspection_endpoint":"https://login.e-infra.cz/oidc/introspect",
    "scopes_supported":[
        "openid",
        "profile",
        "email",
        "address",
        "phone",
        "offline_access"
    ],
    "issuer":"https://login.e-infra.cz/oidc/",
    "userinfo_encryption_enc_values_supported":[
        "XC20P",
        "A256CBC+HS512",
        "A256GCM",
        "A192GCM",
        "A128GCM",
        "A128CBC-HS256",
        "A192CBC-HS384",
        "A256CBC-HS512",
        "A128CBC+HS256"
    ],
    "id_token_encryption_enc_values_supported":[
        "XC20P",
        "A256CBC+HS512",
        "A256GCM",
        "A192GCM",
        "A128GCM",
        "A128CBC-HS256",
        "A192CBC-HS384",
        "A256CBC-HS512",
        "A128CBC+HS256"
    ],
    "authorization_endpoint":"https://login.e-infra.cz/oidc/authorize",
    "service_documentation":"https://login.e-infra.cz/oidc/about",
    "request_object_encryption_enc_values_supported":[
        "XC20P",
        "A256CBC+HS512",
        "A256GCM",
        "A192GCM",
        "A128GCM",
        "A128CBC-HS256",
        "A192CBC-HS384",
        "A256CBC-HS512",
        "A128CBC+HS256"
    ],
    "device_authorization_endpoint":"https://login.e-infra.cz/oidc/devicecode",
    "userinfo_signing_alg_values_supported":[
        "HS256",
        "HS384",
        "HS512",
        "RS256",
        "RS384",
        "RS512",
        "ES256",
        "ES384",
        "ES512",
        "PS256",
        "PS384",
        "PS512"
    ],
    "claims_supported":[
        "sub",
        "name",
        "preferred_username",
        "given_name",
        "family_name",
        "middle_name",
        "nickname",
        "profile",
        "picture",
        "website",
        "gender",
        "zoneinfo",
        "locale",
        "updated_at",
        "birthdate",
        "email",
        "email_verified",
        "phone_number",
        "phone_number_verified",
        "address"
    ],
    "claim_types_supported":[
        "normal"
    ],
    "op_policy_uri":"https://login.e-infra.cz/oidc/about",
    "token_endpoint_auth_methods_supported":[
        "client_secret_post",
        "client_secret_basic",
        "client_secret_jwt",
        "private_key_jwt",
        "none"
    ],
    "token_endpoint":"https://login.e-infra.cz/oidc/token",
    "response_types_supported":[
        "code",
        "token"
    ],
    "request_uri_parameter_supported":false,
    "userinfo_encryption_alg_values_supported":[
        "RSA-OAEP-512",
        "RSA-OAEP",
        "RSA-OAEP-256",
        "RSA1_5",
        "RSA-OAEP-384"
    ],
    "grant_types_supported":[
        "authorization_code",
        "implicit",
        "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "client_credentials",
        "urn:ietf:params:oauth:grant_type:redelegate",
        "urn:ietf:params:oauth:grant-type:device_code",
        "refresh_token"
    ],
    "end_session_endpoint":"https://login.e-infra.cz/oidc/endsession",
    "revocation_endpoint":"https://login.e-infra.cz/oidc/revoke",
    "userinfo_endpoint":"https://login.e-infra.cz/oidc/userinfo",
    "token_endpoint_auth_signing_alg_values_supported":[
        "HS256",
        "HS384",
        "HS512",
        "RS256",
        "RS384",
        "RS512",
        "ES256",
        "ES384",
        "ES512",
        "PS256",
        "PS384",
        "PS512"
    ],
    "op_tos_uri":"https://login.e-infra.cz/oidc/about",
    "require_request_uri_registration":false,
    "code_challenge_methods_supported":[
        "plain",
        "S256"
    ],
    "id_token_encryption_alg_values_supported":[
        "RSA-OAEP-512",
        "RSA-OAEP",
        "RSA-OAEP-256",
        "RSA1_5",
        "RSA-OAEP-384"
    ],
    "jwks_uri":"https://login.e-infra.cz/oidc/jwk",
    "subject_types_supported":[
        "public",
        "pairwise"
    ],
    "id_token_signing_alg_values_supported":[
        "HS256",
        "HS384",
        "HS512",
        "RS256",
        "RS384",
        "RS512",
        "ES256",
        "ES384",
        "ES512",
        "PS256",
        "PS384",
        "PS512",
        "none"
    ],
    "registration_endpoint":"https://login.e-infra.cz/oidc/register",
    "request_object_signing_alg_values_supported":[
        "HS256",
        "HS384",
        "HS512",
        "RS256",
        "RS384",
        "RS512",
        "ES256",
        "ES384",
        "ES512",
        "PS256",
        "PS384",
        "PS512"
    ],
    "request_object_encryption_alg_values_supported":[
        "RSA-OAEP-512",
        "RSA-OAEP",
        "RSA-OAEP-256",
        "RSA1_5",
        "RSA-OAEP-384"
    ]
}
    """

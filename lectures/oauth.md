# OAuth 2.0 Authorization Framework

The OAuth 2.0 authorization framework is defined in the [RFC 6739](https://datatracker.ietf.org/doc/html/rfc6749).
Read the following tutorials to gain foundational knowledge of the OAuth 2.0 authorization framework:

- [Understand OAuth 2.0 at a high level](https://github.com/SAP-samples/cloud-apis-virtual-event/tree/main/exercises/02)
- [An Introduction to OAuth 2](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2).

## OAuth authentication flow

To delve deeper into OAuth 2.0, we will manually explore the authentication flows
using [Microsoft Graph API 🕸️](https://learn.microsoft.com/en-us/graph/) as an example.
For a initial exploration of the API use the [Microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer).
The Graph API provides to authentication methods:

- Delegated Access
- App-only Access
  These correspond to the _authorization code_ and _client credentials_ grant types of the OAuth 2.0 specification.

Next we will use tools like [HTTPie](https://httpie.io/) or [Postman](https://www.postman.com/) to perform the authentication flow.
The code snippets can be used to get started using [HTTPie](https://httpie.io/).

## Prerequisites

Before requesting access tokens, register your app with the Microsoft identity platform. j
Follow the steps outlined
[here](https://learn.microsoft.com/en-us/graph/auth/auth-concepts#register-the-application).

## Grant Type Authorization Code

The grant type authorization code allows a client to request authorization on behalf of the user. The authentication flow for this
grant type involves three steps:

1. Request authorization
2. Request access token
3. Access service

### Request authorization

To request authorization an app needs to redirect the user to the `/authorize` endpoint of the Microsoft identity platform.
In the example below an authorization code (`response_type=code`) is requested for the `scope` `user.read`. The resulting token is
returned to the app using a query (`response_mode=query`). This is where the [redirect URL](https://learn.microsoft.com/en-us/graph/auth-register-app-v2#add-a-redirect-uri)
added when registering the app becomes relevant. The identity platform uses this URL to return the
authorization code.

```bash
https://login.microsoftonline.com/{tenant}/oauth2/v2.0/authorize?client_id={client}&response_type=code&scope=user.read&response_mode=query
```

> **Hint**
> A simple Web server can be started locally using
> `python3 -m http.server`

### Request access token

To request a access token a POST request is invoked at the `/token` endpoint. This request returns a
JSON object containing the assess token as well as additional information like the token type and the scope.

```bash
https -v -f POST https://login.microsoftonline.com/$TENANT_ID/oauth2/v2.0/token \
                 client_id=$CLIENT_ID \
                 client_secret=$CLIENT_SECRET \
                 code=$AUTH_CODE \
                 grant_type=authorization_code \
                 scope=user.read
```

### Call a Microsoft Graph service

Using the access token it is now possible to invoke different services in the Microsoft Graph API. The example blow shows
how to get the profile information for the currently logged in user.

```bash
https -v -A bearer -a $TOKEN https://graph.microsoft.com/v1.0/me
```

## Exercises

1. Try to log in using a different user and access the same service. What do you observe.
1. Attempt to retrieve other information, like a user's email. If unsuccessful, what changes are necessary?
1. What occurs when an access token expires? How can an app obtain a new token?

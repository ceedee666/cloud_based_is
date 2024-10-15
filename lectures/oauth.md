# OAuth 2.0 Authorization Framework

The OAuth 2.0 authorization framework is defined in the [RFC
6739](https://datatracker.ietf.org/doc/html/rfc6749). Read the following
tutorials to gain foundational knowledge of the OAuth 2.0 authorization
framework:

- [Understand OAuth 2.0 at a high
  level](https://github.com/SAP-samples/cloud-apis-virtual-event/tree/main/exercises/02)
- [An Introduction to OAuth
  2](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2).

## OAuth 2.0 authentication flow

In this lecture, we will manually explore OAuth 2.0 authentication flows using
[Auth0](https://auth0.com/) as the identity provider. Auth0 offers various
authentication flows and tools to help manage and secure your application's
authentication needs.

To explore the API in practice, we can use tools such as
[Postman](https://www.postman.com/), [HTTPie](https://httpie.io/), or [VS Code
REST
Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
to manually perform OAuth flows.

Auth0 supports different OAuth 2.0 grant types, including:

- **Authorization Code Grant**: For web or native apps where users authenticate
  and provide consent.
- **Client Credentials Grant**: For machine-to-machine communication without
  user interaction.

Next, we’ll walk through examples of both of these flows using Auth0. The code
snippets below can be used to get started using [HTTPie](https://httpie.io/).

## Prerequisites

Before you can request access tokens from Auth0, you need to:

1. Sign up for an Auth0 account at [Auth0 Signup](https://auth0.com/signup).
2. Create a new application in the Auth0 dashboard following [this
   guide](https://auth0.com/docs/get-started/auth0-overview/create-applications/regular-web-apps).
3. Create two example users for this application in the _User Management_.

## Grant type authorization code

The authorization code grant allows a client to request authorization on behalf
of a user. The flow consists of three main steps:

1. Request authorization
2. Exchange authorization code for access token
3. Access the service

### Step 1: Request authorization

To request authorization, the client needs to redirect the user to Auth0’s
`/authorize` endpoint. Here’s an example of how to set up the authorization
request for the `scope` `openid profile email`, with the response type `code`:

```bash
https://YOUR_DOMAIN/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope=openid profile email
```

> **Hint**
>
> The following code snippet can be used to start a simple Web server accepting
> connections on the `/auth` endpoint.
>
> ```python
> from fastapi import FastAPI
>
> app = FastAPI()
>
>
> @app.get("/")
> async def root():
>    return {"message": "Hello World"}
>
>
> @app.get("/auth")
> async def auth(code: str):
>    print(code)
>    return "OK"
> ```
>
> Save the code to a file named `main.py` and run it using `uvicorn main:app`.

### Request access token

> **Hint: Using .env files**
>
> To securely store sensitive values like `$CLIENT_ID` and `$CLIENT_SECRET` and
> to make them easily accessible when using HTTPie you can follow these steps.
>
> - Step 1: Create a `.env` File
>
>   - In your project directory, create a file named `.env`.
>   - Add your Auth0 credentials like this:
>
>     ```bash CLIENT_ID=your_auth0_client_id_here
>     CLIENT_SECRET=your_auth0_client_secret_here
>     DOMAIN=your_auth0_domain_here
>     REDIRECT_URI=https://your_redirect_url_here
>     ```
>
>     The `DOMAIN` should be your Auth0 domain, which looks like
>     `your-tenant-name.us.auth0.com`.
>
> - Step 2: Source the `.env` File in Your Shell
>
>   Before running your HTTPie commands, load the environment variables into
>   your shell session by sourcing the `.env` file:
>
>   `bash source .env`
>
>   This will make the variables available to all your shell commands.
>
> - Step 3: Use the Variables with HTTPie
>
>   You can now reference these variables in e.g. your HTTPie requests as
>   shown in the snippet below:
>
>   ```bash
>   http POST https://$DOMAIN/oauth/token \
>     client_id=$CLIENT_ID ...
>   ```

Next, the authorization code is exchanged for an access token by making a POST
request to the `/oauth/token` endpoint of Auth0. Here’s how to request the
token:

```bash
https -v POST https://$DOMAIN/oauth/token \
       grant_type=authorization_code \
       client_id=$CLIENT_ID \
       client_secret=$CLIENT_SECRET \
       code=$AUTH_CODE \
       redirect_uri=$REDIRECT_URI
```

The response will contain the access token, which can be used to access
protected resources. For example, we will be using the access token to read the
user's profile data.

The token is a [JWT](https://datatracker.ietf.org/doc/html/rfc7519), and you
can decode it using tools like
[jwt-cli](https://www.npmjs.com/package/jwt-cli).

### Access protected resources

Once you have the access token, you can access protected resources. For
instance, to get the user’s profile data:

```bash
https -v GET https://$DOMAIN/userinfo \
      Authorization:"Bearer $ACCESS_TOKEN"
```

## Exercises

1. Try to log in using a different user and access the same service. What do
   you observe?
1. What happens if you change `scope` variable of the initial authorization
   request?
1. What occurs when an access token expires? How can an app obtain a new token?
1. Try to access a service using the Client Credentials grant type. What is
   different?

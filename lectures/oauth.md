# OAuth 2.0

The OAuth 2.0 authorization framework is defined in the [RFC 6739](https://datatracker.ietf.org/doc/html/rfc6749).
The following tutorials are helpful to get some basic understanding of OAuth 2.0:

- [Understand OAuth 2.0 at a high level](https://github.com/SAP-samples/cloud-apis-virtual-event/tree/main/exercises/02)
- [An Introduction to OAuth 2](https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2).

## OAuth authentication flow

To get a more detailed understanding of OAuth 2.0 we will perform an authentication flow manually in the lecture.
Again, the [Twitter API 🐦](https://developer.twitter.com/en/docs/twitter-api) will be used as an example. The
authentication using the grant type Client Credentials is described in [this document](https://developer.twitter.com/en/docs/authentication/oauth-2-0).

To perform the authentication flow you should use a tool like [HTTPie](https://httpie.io/) or [Postman](https://www.postman.com/).
The following code snippets provide a staring point for creating the necessary requests using [HTTPie](https://httpie.io/):

```bash
# Get Access Token:
http -a <api key>:<api key secret> POST 'https://api.twitter.com/oauth2/token?grant_type=client_credentials'

# Invoke the API
http -A bearer -a <bearer token> "https://api.twitter.com/2/tweets/search/recent?query=from:ceedee666"
```

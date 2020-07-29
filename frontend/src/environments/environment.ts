export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'dev-r2v8kom9', // the auth0 domain prefix
    audience: 'coffeeShop', // the audience set for the auth0 app
    clientId: 'JQzfDDyl9mbkxw0p73d8fwXxlK5xQSwV', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};

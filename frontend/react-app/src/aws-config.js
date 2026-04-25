const awsConfig = {
  Auth: {
    Cognito: {
      userPoolId: 'ap-south-1_pCLScUeec',         // e.g., ap-south-1_xxxxxxxxx
      userPoolClientId: '6ef0nlc0gf9guia6qrua10sqn6',  // e.g., 1a2b3c4d5e6f7g8h9i0j1k2l3m
      loginWith: {
        email: true,
      },
    }
  }
};

export default awsConfig;

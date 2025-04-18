# API Credentials Guide and Transfer Instructions

## Table of Contents
1. [OpenAI API Key Setup](#openai-api-key-setup)
2. [Groq API Key Setup](#groq-api-key-setup)
3. [Pinecone API Key Setup](#pinecone-api-key-setup)
4. [Environment Variables Setup](#environment-variables-setup)
5. [Security Best Practices](#security-best-practices)

## OpenAI API Key Setup

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign in or create an account
3. Navigate to API section
4. Click on your profile icon → "View API Keys"
5. Click "Create New Secret Key"
6. Copy and save the key immediately (it won't be shown again)
7. Replace the existing key in `.env`:
   ```
   OPENAI_API_KEY="your-new-key-here"
   ```

## Groq API Key Setup

1. Visit [Groq Console](https://console.groq.com/)
2. Create an account or sign in
3. Go to API Keys section
4. Generate a new API key
5. Copy the key and update in `.env`:
   ```
   GROQ_API_KEY="your-new-groq-key"
   ```

## Pinecone API Key Setup

For each project (Ghana and Sierra Leone):

1. Go to [Pinecone Console](https://app.pinecone.io/)
2. Sign in or create an account
3. Create a new project or select existing
4. Navigate to API Keys section
5. Generate new API key
6. Update the respective keys in `.env`:
   ```
   GHANA_PINECONE_API_KEY="your-new-ghana-key"
   SIERRA_LEONE_PINECONE_API_KEY="your-new-sierra-leone-key"
   ```

## Environment Variables Setup

1. Create or modify `.env` file in project root
2. Add all API keys following this format:
   ```
   OPENAI_API_KEY="your-key"
   GROQ_API_KEY="your-key"
   GHANA_PINECONE_API_KEY="your-key"
   SIERRA_LEONE_PINECONE_API_KEY="your-key"
   ```
3. Never commit `.env` file to version control
4. Keep a template file `.env.example` with dummy values

## Security Best Practices

1. **Never share API keys** publicly or commit them to version control
2. Rotate keys periodically (every 30-90 days)
3. Use environment variables instead of hardcoding
4. Set up proper access controls and permissions
5. Monitor API usage regularly
6. Keep backup copies of keys in a secure password manager
7. Use different keys for development and production

## Transferring Credentials

When transferring the project to a new team:

1. Create new API keys for each service
2. Share keys securely (encrypted channels or password managers)
3. Revoke old keys after confirming new ones work
4. Update documentation with new key holders
5. Never transfer keys via plain text email or public channels

## Important Notes

- Dataset keys should remain unchanged
- All other API keys should be replaced with new ones
- Keep track of key rotation dates
- Document any API usage limits or restrictions
- Test new keys in development before production use

## Emergency Contacts

In case of compromised credentials:
1. OpenAI Support: https://help.openai.com
2. Groq Support: https://console.groq.com/support
3. Pinecone Support: https://docs.pinecone.io/support

Remember to immediately revoke compromised keys and generate new ones if any security breach is suspected. 
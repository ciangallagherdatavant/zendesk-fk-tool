# How to Reset Your Password

## Overview
This article explains how to reset your password in the Tokenization 
platform. Follow the steps below to regain access to your account.

## Before You Begin
Make sure you have access to the email address associated with your 
account. If you do not have access to that email, contact your system 
administrator.

## Steps to Reset Your Password

1. Go to the login page of the Tokenization platform
2. Click the link that says Forgot Password
3. Enter your email address in the field provided
4. Click Submit
5. Check your email for a reset link
6. Click the link in the email
7. Enter your new password
8. Click Save

## Code Example
```bash
curl -X POST https://api.example.com/reset-password \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com"}'
Notes
![Password reset screen screenshot]
Passwords must be at least 8 characters long. They must contain one
uppercase letter, one number, and one special character. If you do
not receive the email within 5 minutes, check your spam folder.
Related Articles

How to update your profile
How to contact support

Copy
6. Press **Command + S** to save

---

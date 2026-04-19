# Free Cloud Deployment Guide

## Overview
This application is deployed using:
- **Frontend**: Vercel/Netlify (React + Vite)
- **Backend**: Render.com (Flask)
- **Database**: PostgreSQL (Render.com)

All services have free tiers with no credit card required for basic usage.

## Frontend Deployment (Vercel or Netlify)

### Option 1: Vercel
1. Push your code to GitHub
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project" and import your repository
4. Select the `frontend/Middle_Ground` folder as root directory
5. Environment Variables:
   ```
   VITE_API_BASE_URL=https://debate-coach-backend.onrender.com
   ```
6. Click Deploy

### Option 2: Netlify
1. Push your code to GitHub
2. Go to [netlify.com](https://netlify.com)
3. Click "New site from Git" and connect your repo
4. Build Settings:
   - Build command: `npm run build`
   - Publish directory: `dist`
   - Base directory: `frontend/Middle_Ground`
5. Environment Variables:
   ```
   VITE_API_BASE_URL=https://debate-coach-backend.onrender.com
   ```
6. Deploy

## Backend Deployment (Render.com)

### Prerequisites
- Python 3.11
- PostgreSQL database (included in Render free tier)

### Steps
1. Push your code to GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" and select "Web Service"
4. Connect your GitHub repository
5. Settings:
   - Name: `debate-coach-backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Region: Choose closest to you
   - Plan: Free (should auto-select)
6. Create Web Service

### Database Setup (Render.com)
1. From Render dashboard, click "New +" → "PostgreSQL"
2. Name: `debate-db`
3. Database: `debate_db`
4. User: `debate_user`
5. Plan: Free
6. Create Database
7. Copy the Internal Database URL
8. In your Web Service settings, add Environment Variable:
   ```
   DATABASE_URL=<paste-internal-database-url>
   GROQ_API_KEY=<your-groq-api-key>
   ```

### Connect Database to Backend
1. In Render dashboard, go to your Web Service
2. Go to "Environment" tab
3. Add `DATABASE_URL` pointing to your PostgreSQL database
4. Redeploy

## Environment Variables

### Backend (.env or Render Environment)
```bash
DATABASE_URL=postgresql://user:password@host/database
GROQ_API_KEY=your_groq_api_key
FLASK_ENV=production
```

### Frontend (.env or Vercel/Netlify)
```bash
VITE_API_BASE_URL=https://debate-coach-backend.onrender.com
```

## Costs
- Render.com: Free tier includes 1GB RAM, database included
- Vercel/Netlify: Free tier includes unlimited deployments
- Total Cost: **$0/month** for basic usage

## Monitoring

### Backend Logs (Render)
1. Go to your Web Service in Render
2. Click "Logs" tab to see real-time logs
3. Check for errors and application output

### Database (Render)
1. Go to your PostgreSQL database in Render
2. Click "Connect" for connection info
3. Use psql or admin tool to check data

## Scaling

When you outgrow the free tier:
- **Backend**: Upgrade to Paid tier on Render ($7/month)
- **Database**: Upgrade to Standard tier on Render ($15/month)
- **Frontend**: Vercel/Netlify Pro ($20/month, optional)

## Troubleshooting

### Backend not connecting to database
1. Check `DATABASE_URL` is correct in Render environment
2. Verify database is running (check Render PostgreSQL status)
3. Check logs in Render for errors

### Frontend API calls failing
1. Verify `VITE_API_BASE_URL` environment variable
2. Check CORS settings in Flask backend (should be enabled)
3. Check browser console for error messages

### Application crashes
1. Check Render logs for error messages
2. Ensure all environment variables are set
3. Verify `requirements.txt` has all dependencies

## Local Development

To run locally before deploying:

```bash
# Install dependencies
cd backend
pip install -r requirements.txt

# Set environment variables
export DATABASE_URL=sqlite:///debate.db
export GROQ_API_KEY=your_key

# Run backend
python app.py

# In another terminal
cd frontend/Middle_Ground
npm install
npm run dev
```

Then visit http://localhost:5173 (frontend) and http://localhost:5000 (backend)

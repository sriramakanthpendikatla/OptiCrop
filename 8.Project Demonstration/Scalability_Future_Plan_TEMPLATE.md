# Scalability & Future Plan (fill in your real details)

## Scalability Considerations
- Current: single Logistic Regression model served via Flask, works for the given dataset size.
- To scale: containerize with Docker, deploy behind a proper WSGI server (gunicorn),
  add caching, and consider a managed DB if user data storage is added.

## Future Plan
- Compare against ensemble models (Random Forest, XGBoost)
- Add soil-type / geographic-region features
- Build a REST API for third-party integration
- Add user accounts to track prediction history

Replace/expand with your team's real roadmap, then export/save as PDF.

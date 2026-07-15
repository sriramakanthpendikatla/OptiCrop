# OptiCrop: Scalability & Future Plan

## Scalability Considerations
- Current: a single Logistic Regression model served via Flask, suitable for the current dataset size.
- To scale: containerize with Docker, deploy behind a production WSGI server (gunicorn),
  add caching, and consider a managed database if user data storage is added.

## Future Plan
- Compare against ensemble models (Random Forest, XGBoost).
- Add soil-type / geographic-region features.
- Build a REST API for third-party integration.
- Add user accounts to track prediction history.

# Challenge docs

I opted for models with balance because they provide a better trade-off between the two classes. Although models without balance offer higher accuracy, they significantly underperform on class 1, which can be critical depending on the use case. When both classes are important, models with balance are more suitable as they maintain a reasonable trade-off between precision and recall for both classes. The models without balance appears to be overfitting to class 0, likely due to the class imbalance in the data.


For production, I decided to use **XGBClassifier** with balance, as it shows a slight performance advantage over logistic regression in terms of **F1-score**. While the improvement is minor, XGBoost tends to handle larger datasets and more complex feature relationships better than logistic regression, providing greater flexibility for future tuning. This makes it a more robust and scalable option in scenarios with higher data complexity.


The link to the API is as follows: 

http://mlb-80-274378231.us-east-2.elb.amazonaws.com/health



## Cloud

I chose **AWS ECR, ECS, and Fargate** for deploying my API because they simplify containerized deployments while offering scalability and cost efficiency. ECR handles the container image storage, ensuring seamless integration with ECS, which orchestrates the deployment of the API. 

## Handling of Validation Errors in FastAPI

I implemented a custom exception handler for **RequestValidationError** to return a **400 Bad Request** status code instead of the default **422 Unprocessable Entity**, which FastAPI typically uses for validation errors. This was required to meet specific **API design requirements**, where the client expects validation errors to be indicated with a 400 status code.
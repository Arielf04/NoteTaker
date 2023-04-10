Stat210:Week6 10/47

- Model development cycle: Initial model, model diagnostics, remedial measures, consider competing models
- Two classic datasets: Fuel efficiency of cars, software development complexity
- Model selection: If considering multiple models, which one is best? Model selection versus model-averaging
- Fuel efficiency of cars dataset: Mileage and weight variables
- Software development complexity dataset: Work hours and function point count
- Remedial measures: Fixing initial model if needed, look at problem with linearity, nonconstant variance, and outliers
None
New run:


0) 0 Stat210:Week6 15/47Bullet points:

• Linear regression is very flexible and can be used to model any combination of predictor variables
• Other tools, such as nonlinear regression and GLMs, can be used to better match the data
• Simple transformations can also help, such as modeling logy or y instead of y
• It can be difficult to know what model to fit and how to use complex tools in practice
None
New run:


▶ Examine data ▶ Check for errors ▶ Check for special circumstances ▶ Consider other models ▶ Consider other transformations Stat210:Week6 22/47Outliersandinfluentialpoints Influential points Consider these following (simulated) data ▶ Scatterplot and residual plot 8 4 6 slaudiser 2 y 4 dezitnedutS 0 2 2− 0 −2 −1 0 1 2 1 2 3 4 5 x Fitted values Stat210:Week6 23/47Outliersandinfluentialpoints Influential points: remedial measures Apparent influential point ▶ Q: What should we do about it? ▶ A: It depends Best approach ▶ Examine data ▶ Check for errors ▶ Check for special circumstances ▶ Consider other models ▶ Consider other transformations Stat210:Week6 24/47     

Bullet Points:
- Non-linear regression (single predictor) can be used to model data.
- Transformations of y can sometimes be used to ‘linearise’ the model.
- Polynomial regression can be used to model data, but it is important to standardize the predictors and be aware of the dangers of extrapolation.
-
None
New run:


Stat210:Week6 26/47Bullet Points:

▶ Investigate outliers:
  - Is it an obvious mistake? If so, remove
  - Is there anything unusual about it?
  - Is there a lurking variable that explains it?
▶ Understand if it is an influential point:
  - Observations further from the mean predictor (x) value are more likely to be influential
  - Does removing this point make a difference?
  - Does it change the estimates of the parameters?
  - Does it change the confidence intervals?
▶ If it is not influential, there is little harm in leaving it in the dataset
▶ Present a ‘sensitivity’ analysis to demonstrate how much results rely on unusual datapoints
None
New run:


Consider which variables may have interactions Principle 4: ▶ Think about the expected sign of the predictors 

- Variability in data may increase with fitted values, which can be remedied with a transformation or more complex statistical models
- Model building principles include: considering all predictor variables that may be important, checking variables for correlation, considering which variables may have interactions, and thinking about the expected sign of the predictors
- Log and other transforms are common to use for positive data, but can affect linearity
- Weighted least squares and generalised linear models are alternative approaches for nonconstant variance
None
New run:


remaining predictors are significant Modelbuildingandselection Backwardselection What variables to keep? Backward selection Start with all predictors in the model: Bullet Point Summary: 
• When determining which variables to keep in a model, consider Gelman and Hill's (2007) principles which involve looking at the p-value and sign of each estimated effect
• If the predictor is not significant and has unexpected sign, remove it from the model
• If the predictor is significant and has expected sign, leave it in
• If the predictor is significant but has unexpected sign, consider if there are lurking variables
• Alternatives to this approach include forward/backward/stepwise selection, Akaike's Information Criterion, Penalized regression, and Cross-validation
None
New run:


All predictors you think may be affecting outcomeBullet Points: 
- Backward and stepwise selection are early examples of computer-driven model selection that do not require large sample sizes
- Backward selection starts with all predictors in the model and removes the predictor with the largest p-value
- Stepwise selection combines elements of forward and backward selection, where variables are added or subtracted at each step
- It is recommended to specify a "basic" and "full" model and consider a handful of other models between these two
- AIC can be used to narrow down the selection of models to a small number of possible models
None
New run:


interactions between these variables. Stat210:Week6 41/47

- Recommend specifying a “basic” model (bare minimum you can justify scientifically) and a “full” model (all predictors you think may be affecting outcome)
- Consider a handful of other models between these two
- Calculate AIC for each candidate model (“score” that estimates predictive performance of model)
- Choose model with lowest AIC score (relative difference is important)
- Or, may combine results from multiple models (model-averaging)
- Avoid forwards/backwards/stepwise selection
None
New run:


• Model building and selection approaches (G & H, stepwise, AIC) are used to choose the best model
• Value in considering more than one model
• Remedial measures to fix 'broken' models include adding predictor variables, transforming variables, and identifying/removing outliers
None
PS E:\NoteTaker> & C:/Users/Admin/AppData/Local/Microsoft/WindowsApps/python3.10.exe e:/NoteTaker/gui.py
New run:


(e.g. quadratic) Technical answer (in R): ▶ Use nonlinear regression ▶ Use a transformation ▶ Use a GAM (Generalized Additive Model) Stat210:Week6 10/47

- Stat210 is a course at the University of Otago
- The course covers model development and selection
- Two datasets are used to focus on remedial measures and model selection: fuel efficiency of cars and software development complexity
- Model development cycle involves initial model, model diagnostics, remedial measures, and consideration of competing models
- Model selection is the process of determining which model is best
- Model selection is different from model-averaging
- Remedial measures involve fixing the initial model if needed
- This can be done by fitting a better model, using nonlinear regression, using a transformation, or using a GAM (Generalized Additive Model)
None
New run:


0) 0 Summary 
- Linear regression is a flexible tool that allows us to fit any model that can be written in the form of y = βf(x1, ..., xk)+ε, where β are parameters and f are functions of data.
- We can add any combination of predictor variables to our model to fix the response shape.
- We can also consider transformations of the response, such as y∗ = g(y), to affect both the shape and variance of the response.
- Linear regression is linear in terms of β parameters, meaning that we can include any function of xj in the model, such as x, x2, x3, log(x).
- We can also use transformations of y to ‘linearise’ the model.
None
New run:


▶ Try to understand why it is there ▶ If it is an error, remove it from the data set ▶ If it is not an error, leave it in the data set Stat210:Week6 22/47

Flexibility of Regression:
- Non-linear regression (single predictor)
- Non-linear regression examples:
  - y =β0eβ1x+ϵ
  - y = β1x +ϵ β2+x
  - y =β0eβ1xϵ
  - y =β0eβ1x+ϵ
- Sometime can use transformations of y to ‘linearise’ the model
  - First model: y =β0eβ1x+ϵ →logy =logβ0+β1x+ϵ, or y∗ =β∗+β x+ϵ 0 1 (where y∗ =logy, β∗ =logβ ) 0 0
  - Second model: no transformation can make it linear – use nonlinear regression nls
  - Third model: transformation works, if logϵ∼N(0,σ2)
  - Fourth model: transformation can make the mean response linear but leads to a different error structure – not quite the same model (but meets nls assumptions)

Polynomial regression:
- Mileage data
- Estimate Std. Error t value Pr(>|t|) (Intercept) 8.08 0.24 33.05 0.00 weight -2.43 0.21 -11.46 0.00 weight2 0.48 0.15 3.26 0.00
- The slope of the line changes as x changes
- Just plot the line (interpreting β and β is tricky) 1 2
- Normally standardize predictors if fitting polynomial regression
  - Reduces correlation
  - Helps avoid multicollinearity
- Extrapolation is especially dangerous
  - Dangerous in any regression model
  - Especially so for polynomial models
  - Curve is only appropriate over range of x observed
  - Any regression model is only an approximation
  - Describe the relationship
None
New run:


Stat210:Week6 26/47

Summary:

- Outliers should be investigated to determine if they are an obvious mistake or if there is something unusual about the observation.
- If there is a lurking variable that helps explain the observation, it should be included in the model.
- Observations further from the mean predictor value are more likely to be influential and should be examined to determine if they should be removed.
- If removing the observation does not make a difference, there is little harm in leaving it in the dataset.
- A sensitivity analysis can be performed to demonstrate how much the results rely on unusual datapoints.
None
New run:


Consider which variables may have interactions Principle 4: ▶ Think about the expected sign of the predictors

- When dealing with nonconstant variance, two approaches can be taken: transformation (e.g. log and transforms) or more complex statistical models
- When building models, consider all predictor variables that may be important, check for correlation between variables, consider which variables may have interactions, and think about the expected sign of the predictors    
- In the example given, a log-log model was specified for hours and count, and it was found that there was no pattern or evidence of nonconstant variance, and no extreme outliers
None
New run:


remaining predictors have p-values smaller than the chosen α Modelbuildingandselection Backwardselection What variables to keep? Backward selection Start with the full model containing all p predictors

- Approach based on principles of Gelman and Hill (2007): Look at statistical significance (p-value) and sign of each estimated effect:
  - If a predictor is not significant and has unexpected sign, remove it from the model
  - If a predictor is not significant but has expected sign, generally fine to leave it in
  - If a predictor is significant and has expected sign, leave it in
  - If a predictor is significant but has unexpected sign, think hard about the science underlying the problem
- Forward selection: Start with no predictors in the model and consider all p possible predictors one-at-a-time, include the predictor with smallest p-value, consider all p−1 remaining predictors one-at-a-time, include the predictor with smallest p-value, repeat until no significant predictors are left
- Backward selection: Start with the full model containing all p predictors, refit the model with remaining p−1 predictors, remove the predictor with the largest p-value, repeat until all remaining predictors have p-values smaller than the chosen α
None
New run:


All predictors you think may be affecting outcome

- Backward selection: Start with all predictors in the model, remove the predictor with the largest p-value, refit the model with remaining p−1 predictors, remove the predictor with the largest p-value, repeat until all remaining predictors are significant

- Stepwise selection: Combine elements of forward and backward selection, where variables are added or substracted at each step, do not require large sample sizes, with large n, other techniques become available (machine learning)

- AIC: Narrow down selection to a small number of possible models (candidate set), recommend specifying “basic” model (bare minimum you can justify scientifically), recommend specifying “full” model (all predictors you think may be affecting outcome), consider a handful of other models between these two (reflect scientific hypotheses you are considering).
None
New run:


interactions between any of these variables.

- Consider underlying science to specify a “basic” and “full” model
- Narrow down selection to a small number of possible models (candidate set)
- Calculate AIC for each candidate model
- AIC is a score that estimates predictive performance of model and accounts for fit of the model to the data, and number of parameters used in model
- Choose model with lowest AIC score, relative difference is important
- Or, may combine results from multiple models (model-averaging)
- Avoid forwards/backwards/stepwise selection
None
New run:


-Model building and selection approaches (G & H, stepwise, AIC) are used to choose the best model.
-Remedial measures to fix ‘broken’ models include adding predictor variables, transforming variables, and identifying and dealing with outliers.
None

# BoilerEfficiencyPredictor 
## Abstract
Machine Learning Algorithm for predicting Boiler efficiency at JSW energy
The properties of coal have a greater impact on the combustion efficiency and operation
efficiency of many equipment of the power plant including pulverizing mills, boiler, air heater,
ESP, ash disposal, the coal handling facilities, as well as stack emissions. The behavior of a coal
in a boiler is strongly influenced by the mineral matter and other impurities associated with it,
both in terms of how much ash-forming material is there, and its composition. In particular, the
mineral matter can form slagging deposits in the hotter parts of the boiler and fouling deposits as
the flue gas passes through the heat exchangers and are progressively cooled.
Various coal properties can affect the efficient and consistent operation of both the boiler
and the emissions control units which clean the flue gases before discharge.
They therefore affect both the short- and long-term operability of the plant, and the economics of
the operation. The major contributor to differences in coal properties is the presence of the
mineral matter.
Our aim for this project is to analyze and predict the effect of various properties of coal
on combustion efficiency, Slagging and fouling indices and effectiveness of electrostatic
precipitators.

First, dataframe object named df has been created that contains the training dataset. Then one of
the rows of the dataframe has been deleted for the sake of convenience in implementation. The
correlation between the input and output parameters has been calculated using the function
pearsonr() that is built in sklearn library. Then the model is trained and a straight line is fitted
through the scatter points. The coefficient matrix and the intercept are then calculated using built
in functions and are printed. Then the algorithm is run on a sample, results are printed and
evaluated using r_squared value

Here, r_squared value is used as a basis for evaluating how well the model fits the data.
R-squared (r² or the coefficient of determination) is a statistical measure in a regression model
that determines the proportion of variance in the dependent variable that can be explained by the
independent variable. In other words, r-squared shows how well the data fit the regression model
(the goodness of fit). r-squared can take any values between 0 to 1. Although the statistical
measure provides some useful insights regarding the regression model, the user should not rely
only on the measure in the assessment of a statistical model. It does not indicate the correctness
of the regression model. Therefore, the user should always draw conclusions about the model by
analyzing r-squared together with the other variables in a statistical model.

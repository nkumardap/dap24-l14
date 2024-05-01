"""
INTRODUCTION

This exercise asks you to play around with multiple models by using a dataset
containing the rates of violent crime per 100,000 residents for various US 
states. We will construct 4 different models and then use a new tool called
summary_col to show them all in a single compact table.
"""

"""
DOCUMENTATION

Title: Statewide Crime Data 2009

Notes: All data is for 2009 and was obtained from the American Statistical 
    Abstracts except as indicated below.
    
    
    Number of observations: 51
    Number of variables: 8
    Variable name definitions:

    state
        All 50 states plus DC.
    violent
        Rate of violent crimes / 100,000 population. Includes murder, forcible
        rape, robbery, and aggravated assault. Numbers for Illinois and
        Minnesota do not include forcible rapes. Footnote included with the
        American Statistical Abstract table reads:
        "The data collection methodology for the offense of forcible
        rape used by the Illinois and the Minnesota state Uniform Crime
        Reporting (UCR) Programs (with the exception of Rockford, Illinois,
        and Minneapolis and St. Paul, Minnesota) does not comply with
        national UCR guidelines. Consequently, their state figures for
        forcible rape and violent crime (of which forcible rape is a part)
        are not published in this table."
    murder
        Rate of murders / 100,000 population.
    hs_grad
        Percent of population having graduated from high school or higher.
    poverty
        % of individuals below the poverty line
    white
        Percent of population that is one race - white only. From 2009 American
        Community Survey
    single
        Calculated from 2009 1-year American Community Survey obtained
        from Census. Variable is Male householder, no wife present, family
        household combined with Female householder, no husband present, family
        household, divided by the total number of Family households.
    urban
        % of population in Urbanized Areas as of 2010 Census. Urbanized
        Areas are area of 50,000 or more people.
"""

"""
EXERCISE 1

One theory posits that a lack of education is responsible for violent crime.

Open the file statecrime.csv Create and estimate a linear model where violent 
crime per 100,000 residents is the endogenous variable and high school 
graduation rate is the exogenous variable.

Name this model "model1".

Use the OLS method from statsmodels:

    from statsmodels.regression.linear_model import OLS

Hint: in the example below, .fit() is immediately applied, and the variable 
named model is now storing the results of this model!

    model = OLS(<content>).fit()

"""

"""
EXERCISE 2

Create model2 and model3, which are similar to model1 except that they look at
the poverty rate and urbanization rates respectively.

Create a model4 which includes all three factors as exogenous variables.
"""

"""
EXERCISE 3

Let's create a single table to show all the resulting coefficients, using the 
summary_col method:

    from statsmodels.iolib.summary2 import summary_col

summary_col has only one positional argument: a list of fitted models to be
shown. Pass a list of all the models we've constructed into this method to
create a table.

Hint: Use the option stars = True to flag all statistically significant 
coefficients.

Hint: You can read more about summary_cols here:
https://tedboy.github.io/statsmodels_doc/generated/statsmodels.iolib.summary2.summary_col.html
"""

"""
EXERCISE 4 (BONUS)

Let's use our fine grained control over the parameters. Change the column
names to something more conventional such as (1), (2) ... and so on. Make it so
that coefficients only round to 2 decimal points.
"""
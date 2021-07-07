# Developer Operations (DevOps)

Development and Operations have been merged to form the new DevOps strategy. This allows for the principle of a Continuous Integration Pipeline. This consists of the following steps;

1. Continuous Integration
2. Continuous Delivery
3. Continuous Deployment

## Continuous Integration (CI)

Continuous integration is the practice of automatic merging of code changes made by members of the development team into a single codebase. It is considered as a Development Operations (DevOps) best practice. This central repository is where builds are made and tests are run. Automated tools then assert the codebase validity before integration. Coding standards, code quality and syntax checks can also be run at this stage.

## Continuous Delivery

Continuous Delivery is the next stage in the CI pipeline, automated build tools create an enduser deliverable package. 

## Continuous Deployment (CD)

Continuous Deployment (CD) is a software release process that uses automated testing to validate if changes to a codebase are correct and stable for immediate autonomous deployment to a production environment. It will deploy if correct and fail new version if wrong.

CD involves the following cycle:

1. Build
2. Test
3. QA (Acceptance Test)
4. Deploy Staging
5. Deploy Production
6. Monitor

Before Continuous Deployment, organisations use to follow the Continuous Delivery process which was manual testing and acceptance after manual merging the new code for staging deployment. After manual tests were passed the code was moved to production or failed.

Continuous Deployment has the following advantages;

1. Fast turnaround for bug fixes
2. Fast implementation of user feature request or changes
3. Fast time-to-market
4. Rapid deployment and testing

Continuous Deployment requirements;

1. Test-driven development
2. Single deployment method
3. Containerisation

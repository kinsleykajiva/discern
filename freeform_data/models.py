from django.db import models

class UserRoles():
    student = "student"
    teacher = "teacher"
    administrator = "administrator"

class EssayTypes():
    test = "test"
    train = "train"

class GraderTypes():
    machine = "ML"
    instructor = "IN"
    peer = "PE"

class Organization(models.Model):
    #TODO: Add in address info, etc later on
    organization_size = models.IntegerField(default=0)
    organization_name = models.TextField()
    #TODO: Add in billing details, etc later, along with rules on when to ask
    premium_service_subscriptions = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class UserProfile(models.Model):
    #TODO: Add in a callback where if user identifies as "administrator", then they can create an organization
    user = models.ForeignKey(User, unique=True, blank=True,null=True)
    #TODO: Potentially support users being in multiple orgs, but will be complicated
    organization = models.ForeignKey(Organization)
    #Add in userinfo here.  Location, etc
    name = models.TextField()
    #User role in their organization
    role = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Course(models.Model):
    #A user can have many courses, and a course can have many users
    users = models.ManyToManyField(UserProfile)
    #Each course has a name!
    course_name = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Problem(models.Model):
    course = models.ForeignKey(Course)
    #Max scores for one or many targets
    max_target_scores = model.TextField()
    #If additional numeric predictors are being sent, the count of them
    number_of_additional_predictors = models.IntegerField()
    #Prompt of the problem
    prompt = models.TextField()
    #If org has subscriptions to premium feedback models
    premium_feedback_models = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Essay(models.Model):
    #Each essay is written for a specific problem
    problem = models.ForeignKey(Problem)
    #Each essay is written by a specified user
    user = models.ForeignKey(UserProfile)
    #Each user writes text (their essay)
    essay_text = models.TextField()
    #Schools may wish to send additional predictors (student grade level, etc)
    additional_predictors = models.TextField()
    #The type of essay
    essay_type = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class EssayGrade(models.Model):
    #Each essaygrade is for a specific essay
    essay = models.ForeignKey(Essay)
    #How the essay was scored for numerous targets
    target_scores = models.TextField()
    #What type of grader graded it
    grader_type = models.CharField(max_length=20)
    #Feedback from the grader
    feedback = models.TextField()
    #Annotated text from the grader
    annotated_text = models.TextField()
    #Scores on premium feedback model, if any
    premium_feedback_scores = models.TextField()
    #whether or not the grader succeeded
    success = models.BooleanField()
    #For peer grading and staff grading, we will use this
    user = models.ForeignKey(UserProfile,blank=True,null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)








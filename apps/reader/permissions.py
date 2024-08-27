from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


# IsAuthenticated = if user is not authenticated, it will fail


# IsAdminUser = 'is_staff' is 'false', it will fail


# IsAuthenticatedOrReadOnly = CRUD

  # POST
  # GET     -> READ no authentication needed
  # PUT, PATCH
  # DELETE

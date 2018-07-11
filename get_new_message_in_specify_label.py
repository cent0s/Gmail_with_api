"""Get a list of Labels from the user's mailbox.
"""

from apiclient import errors


from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# Setup the Gmail API
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
    # creds = None
service = build('gmail', 'v1', http=creds.authorize(Http()))

def ListLabels(service, user_id):
  """Get a list all labels in the user's mailbox.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.

  Returns:
    A list all Labels in the user's mailbox.
  """
  try:
    response = service.users().labels().list(userId='me').execute()
    labels = response['labels']
    for label in labels:
      print('Label id: %s - Label name: %s' % (label['id'], label['name']))
    return labels
  except errors.HttpError, error:
      print('An error occurred: %s' % error)



if __name__ == '__main__':
    ListLabels(service,'me')

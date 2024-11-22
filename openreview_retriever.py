import openreview
import argparse

# change to your venue from the venue list
VENUE_ID = 'robot-learning.org/CoRL/2024/Conference'

def get_all_venues(client):
    venues = client.get_group(id='venues').members
    print('\n'.join(venues))

def get_all_submissions(client):
    submissions = client.get_all_notes(content={'venueid': VENUE_ID} )
    return submissions

def write_submissions_to_file(submissions, output_file, with_abstract=False):
    f = open(output_file, "w")
    print(f"==> Writing submissions to {output_file}")
    for submission in submissions:
        sub_text = ""
        sub_text += "Title: " + submission.content['title']['value'] + "\n"
        sub_text += "URL: " + f'https://openreview.net/forum?id={submission.id}' + "\n"
        if 'TLDR' in submission.content:
            sub_text += "TLDR: " + submission.content['TLDR']['value'] + "\n"
        if 'keywords' in submission.content:
            sub_text += "Keywords: " + ", ".join(submission.content['keywords']['value']) + "\n"
        if with_abstract and ('abstract' in submission.content):
            sub_text += "Abstract: " + submission.content['abstract']['value'].replace("\n", " ") + "\n"
        sub_text += "\n"
        f.write(sub_text)
    f.close()


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Retrieve OpenReview submissions')
    parser.add_argument('--email', type=str, help='OpenReview email')
    parser.add_argument('--password', type=str, help='OpenReview password')
    parser.add_argument('--output_file', type=str, default=None, help='Output file')
    parser.add_argument('--with_abstract', action='store_true', help='Include abstract in the output file')
    args = parser.parse_args()

    client = openreview.api.OpenReviewClient(
        baseurl='https://api2.openreview.net',
        username=args.email, 
        password=args.password)
    
    # get_all_venues(client)

    if args.output_file:
        submissions = get_all_submissions(client)
        write_submissions_to_file(submissions, args.output_file, with_abstract=args.with_abstract)


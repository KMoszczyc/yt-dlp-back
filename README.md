# yt-dlp-back
Simple yt-dlp backend in Python with Flask for my youtube-converter web application, ready for deployment on Heroku.

## Example usage
Make a POST request on https://yt-dlp-back.herokuapp.com/download endpoint with a JSON:

f.e.  
```javascript
{
    "url":"https://www.youtube.com/watch?v=eFTlFPRCytU&t=181s",
    "sessionDir":"rgw45g435g245rgerg/"
}
```

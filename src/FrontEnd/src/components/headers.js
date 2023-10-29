export const headers = new Headers()
export const API = process.env.REACT_APP_API_URL;
headers.append('Content-Type', 'application/json');
headers.append('Accept', 'application/json');
headers.append('Access-Control-Allow-Origin', API);
headers.append('Access-Control-Allow-Credentials', 'true');
headers.append('GET', 'POST', 'OPTIONS', 'PUT', 'DELETE')
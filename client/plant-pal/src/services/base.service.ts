import axios from 'axios';
import { STORAGE_KEYS } from '../utils/constants';

const BASE_API_URL = process.env.REACT_APP_RAPID_API_URL;
const BASE_API_KEY = process.env.REACT_APP_RAPID_API_KEY;
const HOST = process.env.REACT_APP_RAPID_HOST

interface RequestOption {
  method?: string;
  data?: any;
  params?: any;
  headers?: any;
}

const getToken = () => {
  const token = localStorage.getItem(STORAGE_KEYS.AUTH_TOKEN);
  return token;
};

const makeRequest = (
  urlPath: string,
  options: RequestOption,
  useToken?: boolean,
  internal?: boolean,
  isRapid?: boolean
) => {
  const headers = options.headers || {};
  if (useToken) headers['Authorization'] = 'Bearer ' + getToken();
  if (internal) headers['x-api-key'] = BASE_API_KEY;
  if (isRapid){ headers["X-RapidAPI-Key"] = BASE_API_KEY
  headers["X-RapidAPI-Host"] = HOST
}
  const fullUrl = BASE_API_URL + urlPath;
  return axios({ ...options, url: fullUrl, headers: headers });
};

export const apiService = {
  makeRequest: makeRequest,
  get: (urlPath: string, params: any, useToken = true, internal = false, isRapid = false) =>
    makeRequest(urlPath, { method: 'get', params }, useToken, internal, isRapid),
  patch: (urlPath: string, data: any, useToken = true, internal = false, isRapid=false) =>
    makeRequest(urlPath, { method: 'patch', data }, useToken, internal, isRapid),
  post: (urlPath: string, data: any, useToken = true, internal = false, isRapid=false) =>
    makeRequest(urlPath, { method: 'post', data }, useToken, internal, isRapid),
  put: (urlPath: string, data: any, useToken = true, internal = false, isRapid=false) =>
    makeRequest(urlPath, { method: 'put', data }, useToken, internal, isRapid),
  delete: (urlPath: string, useToken = true, internal = false, isRapid=false) =>
    makeRequest(urlPath, { method: 'delete' }, useToken, internal, isRapid)
};

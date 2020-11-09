import http from '@/http-client';

export default {
  fetch() {
    return http.get('/api/county/home').then((response) => response.data);
  },
};

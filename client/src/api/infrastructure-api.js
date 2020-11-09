import http from '@/http-client';

export default {
  fetch(countyId) {
    return http.get(`/api/counties/${countyId}/infrastructure`).then((response) => response.data);
  },
};
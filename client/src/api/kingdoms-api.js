import http from '@/http-client';

export default {
  fetchAll() {
    return http.get(`/api/kingdoms`).then((response) => response.data);
  },
  fetch(id) {
    return http.get(`/api/kingdoms/${id}`).then((response) => response.data);
  },
};

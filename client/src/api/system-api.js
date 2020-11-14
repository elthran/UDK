import http from '@/http-client';

export default {
  currentUser() {
    return http.get('/api/system/current_user').then((response) => response.data);
  },
};

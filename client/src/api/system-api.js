import http from '@/http-client';

export default {
  currentUser() {
    return http.get('/api/system/current_user').then((response) => response.data);
  },
  currentCounty() {
    return http.get('/api/system/current_county').then((response) => response.data);
  },
  currentKingdom() {
    return http.get('/api/system/current_kingdom').then((response) => response.data);
  },
};

import http from '@/http-client'

export default {
  fetch (id) {
    return http.get(`/api/counties/${id}`).then(response => response.data)
  },
}

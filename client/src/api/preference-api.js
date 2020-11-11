import http from '@/http-client'

export default {
  fetch (countyId) {
    return http.get(`/api/counties/${countyId}/preference`).then(response => response.data)
  },
}

import http from '@/http-client'

export default {
  login ({ username }) {
    return http
      .post('/api/authentication/login', { username })
      .then(response => response.data)
  },
  logout () {
    return http.post('/api/authentication/logout').then(response => response.data)
  },
}

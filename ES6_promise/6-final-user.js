// 6-final-user.js

import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName = '', lastName = '', fileName = '') {
  // signUpUser THEN uploadPhoto
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) =>
    results.map((r) => (r.status === 'fulfilled'
      ? { status: 'fulfilled', value: r.value }
      : { status: 'rejected', value: (r.reason instanceof Error ? r.reason.toString() : r.reason) })));
}

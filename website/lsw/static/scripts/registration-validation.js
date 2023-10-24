function setErrorMessages(messages, elementID) {
    let element = document.getElementById(elementID);
    if (element !== null)
        element.innerHTML = messages.join("<br>");
}

function handleFormSubmit(event) {
    let isValid = true;

    // Name validation
    const name = document.getElementById('name-input').value;
    if (name.trim() === '') {
        setErrorMessages(['Name is required.'], 'name-errors');
        isValid = false;
    } else {
        setErrorMessages([], 'name-errors');
    }

    // Primary Email validation
    const primaryEmail = document.getElementById('primary-email-input').value;
    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if (!emailRegex.test(primaryEmail)) {
        setErrorMessages(['Primary Email is invalid or empty.'],
                        'primary-email-errors');
        isValid = false;
    } else {
        setErrorMessages([], 'primary-email-errors');
    }

    // University Email validation
    const universityEmail = document.getElementById('university-email-input').value;
    if (universityEmail != '' && !emailRegex.test(universityEmail)) {
        setErrorMessages(['University email is invalid.'], 'university-email-errors');
        isValid = false;
    } else {
        setErrorMessages([], 'university-email-errors');
    }

    // Student ID validation
    const studentId = document.getElementById('student-id-input').value;
    const studentIdRegex = /^B00\d{6}$/;
    if (studentId.trim() !== '' && !studentIdRegex.test(studentId)) {
        setErrorMessages(
            ['Student ID is invalid. It should follow the format B00xxxxxx.'],
            'student-id-errors');
        isValid = false;
    } else {
        setErrorMessages([], 'student-id-errors');
    }

    // Year of Study validation
    const yearOfStudy = document.getElementById('year-of-study-input').value;
    if (yearOfStudy !== '' && (yearOfStudy < 1 || yearOfStudy > 6)) {
        setErrorMessages(['Year of Study should be between 1 and 6.'],
                        'year-of-study-input');
        isValid = false;
    } else {
        setErrorMessages([], 'year-of-study-errors');
    }

    if (!isValid) {
        event.preventDefault();
    }
}

document.querySelector('form').addEventListener('submit', handleFormSubmit);


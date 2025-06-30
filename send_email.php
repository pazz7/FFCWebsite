<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "pacitabantilan@gmail.com"; // Replace with your email address
    $subject = "New Form Submission";

    $message = "New form submission:\n\n";
    foreach($_POST as $key => $value) {
        $message .= ucfirst(str_replace("_", " ", $key)) . ": " . $value . "\n";
    }

    $headers = "From: webmaster@example.com" . "\r\n" .
    "Reply-To: webmaster@example.com" . "\r\n" .
    "X-Mailer: PHP/" . phpversion();

    if(mail($to, $subject, $message, $headers)) {
        echo "
<script>alert('Form submitted successfully!');</script>";
    } else {
        echo "
<script>alert('An error occurred. Please try again later.');</script>";
    }
}
?>
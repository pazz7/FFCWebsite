<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "pacitabantilan@gmail.com";
    $subject = "New Form Submission";
    
    $message = "New form submission:\n\n";
    foreach($_POST as $key => $value) {
        $message .= ucfirst(str_replace("_", " ", $key)) . ": " . $value . "\n";
    }
    
    // Updated this part
    $from_email = "noreply@fusionfitnessclubph.com";
    $headers = "From: " . $from_email . "\r\n" .
    "Reply-To: " . $from_email . "\r\n" .
    "X-Mailer: PHP/" . phpversion();

    if(mail($to, $subject, $message, $headers)) {
        echo "<script>alert('Form submitted successfully!');</script>";
    } else {
        echo "<script>alert('An error occurred. Please try again later.');</script>";
    }
}
?>
<!DOCTYPE html>
<html lang="en-US" class="no-js">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <title>Fusion Fitness Club &#8211; Join Us</title>

    <link rel="stylesheet" href="js/plugins/goodlayers-core/plugins/fontawesome/font-awesome.css" type="text/css" media="all" />
    <link rel="stylesheet" href="js/plugins/goodlayers-core/plugins/fa5/fa5.css" type="text/css" media="all" />
    <link rel="stylesheet" href="js/plugins/goodlayers-core/plugins/elegant/elegant-font.css" type="text/css" media="all" />
    <link rel="stylesheet" href="js/plugins/goodlayers-core/plugins/ionicons/ionicons.css" type="text/css" media="all" />
    <link rel="stylesheet" href="js/plugins/goodlayers-core/plugins/simpleline/simpleline.css" type="text/css" media="all" />
    <link rel="stylesheet" href="js/plugins/goodlayers-core/plugins/gdlr-custom-icon/gdlr-custom-icon.css" type="text/css" media="all" />
    <link rel="stylesheet" href="js/plugins/goodlayers-core/plugins/style.css" type="text/css" media="all" />
    <link rel="stylesheet" href="js/plugins/goodlayers-core/include/css/page-builder.css" type="text/css" media="all" />
    <link rel="stylesheet" href="js/plugins/mp-timetable/media/css/style.css?ver=2.4.2" type="text/css" media="all" />
    <link rel="stylesheet" href="css/style-core.css" type="text/css" media="all" />
    <link rel="stylesheet" href="css/zyth-style-custom.css" type="text/css" media="all" />

    <link rel="icon" href="upload/cropped-favicon-circle-32x32.png" sizes="32x32" />
    <link rel="icon" href="upload/cropped-favicon-circle-192x192.png" sizes="192x192" />
    <link rel="apple-touch-icon" href="upload/cropped-favicon-circle-180x180.png" />

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
    $(document).ready(function() {
        $('form').on('submit', function(e) {
            // Form will submit normally
        });
    });
    </script>
</head>

<body class="home page-template-default page page-id-14670 theme-zyth gdlr-core-body woocommerce-no-js zyth-body zyth-body-front zyth-full zyth-with-sticky-navigation zyth-blockquote-style-3 gdlr-core-link-to-lightbox" data-home-url="index.html">
    <div class="zyth-body-outer-wrapper">
        <div class="zyth-body-wrapper clearfix zyth-with-transparent-header zyth-with-frame">
            <div class="zyth-page-wrapper" id="zyth-page-wrapper">
                <div class="gdlr-core-page-builder-body">
                    <div class="gdlr-core-pbf-wrapper" style="padding: 100px 0px 100px 0px;" id="gdlr-core-wrapper-1">
                        <div class="gdlr-core-pbf-background-wrap" style="background-color: #0c0c0c;">
                            <div class="gdlr-core-pbf-background gdlr-core-parallax gdlr-core-js" style="background-image: url(upload/Join-US-BG-1.jpg); background-repeat: no-repeat; background-position: top center;" data-parallax-speed="0"></div>
                        </div>
                        <div class="gdlr-core-pbf-wrapper-content gdlr-core-js">
                            <div class="gdlr-core-pbf-wrapper-container clearfix gdlr-core-container">
                                <div class="gdlr-core-pbf-column gdlr-core-column-60 gdlr-core-column-first" data-skin="Plan Form" id="gdlr-core-column-43005">
                                    <div class="gdlr-core-pbf-column-content-margin gdlr-core-js" style="padding: 10px 0px 0px 0px;">
                                        <div class="gdlr-core-pbf-background-wrap"></div>
                                        <div class="gdlr-core-pbf-column-content clearfix gdlr-core-js" style="max-width: 870px;">
                                            <div class="gdlr-core-pbf-element">
                                                <div class="gdlr-core-title-item gdlr-core-item-pdb clearfix gdlr-core-left-align gdlr-core-title-item-caption-bottom gdlr-core-item-pdlr" style="padding-bottom: 20px;">
                                                    <div class="gdlr-core-title-item-title-wrap">
                                                        <h3 class="gdlr-core-title-item-title gdlr-core-skin-title" style="font-size: 48px; font-weight: 600; font-style: italic; letter-spacing: 0px; text-transform: none; color: #ffffff;">
                                                            Join Us<span class="gdlr-core-title-item-title-divider gdlr-core-skin-divider"></span>
                                                        </h3>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="gdlr-core-pbf-element">
                                                <div class="gdlr-core-divider-item gdlr-core-divider-item-normal gdlr-core-item-pdlr gdlr-core-left-align" style="margin-bottom: 55px; margin-left: 5px;">
                                                    <div class="gdlr-core-divider-container" style="max-width: 38px;">
                                                        <div class="gdlr-core-divider-line gdlr-core-skin-divider" style="transform: skewX(150deg); -webkit-transform: skewX(150deg); border-color: rgb(164, 164, 168); border-width: 7px; border-radius: 0px; -moz-border-radius: 0px; -webkit-border-radius: 0px;"></div>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="gdlr-core-pbf-element">
                                                <div class="gdlr-core-text-box-item gdlr-core-item-pdlr gdlr-core-item-pdb gdlr-core-left-align" style="padding-bottom: 40px ;">
                                                    <div class="gdlr-core-text-box-item-content" style="font-size: 18px; text-transform: none; color: #ffffff;">
                                                        <p>Join Fusion Fitness Club today and start your fitness journey!</p>
                                                    </div>
                                                </div>
                                            </div>
                                            <div class="gdlr-core-pbf-element">
                                                <div class="gdlr-core-contact-form-7-item gdlr-core-item-pdlr gdlr-core-item-pdb">
                                                    <div role="form" class="wpcf7" id="wpcf7-f1979-p1964-o1" lang="en-US" dir="ltr">
                                                        <div class="screen-reader-response">
                                                            <p role="status" aria-live="polite" aria-atomic="true"></p>
                                                            <ul></ul>
                                                        </div>
                                                        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post" class="wpcf7-form init" novalidate="novalidate" data-status="init">
                                                            <div class="gdlr-core-input-wrap gdlr-core-full-width gdlr-core-bottom-border gdlr-core-with-column">
                                                                <div class="gdlr-core-column-30">
                                                                    <span class="wpcf7-form-control-wrap your-first-name">
                                                                        <input type="text" name="first_name" value="" size="40" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required" aria-required="true" aria-invalid="false" placeholder="First Name*" required />
                                                                    </span>
                                                                </div>
                                                                <div class="gdlr-core-column-30">
                                                                    <span class="wpcf7-form-control-wrap your-last-name">
                                                                        <input type="text" name="last_name" value="" size="40" class="wpcf7-form-control wpcf7-text wpcf7-validates-as-required" aria-required="true" aria-invalid="false" placeholder="Last Name*" required />
                                                                    </span>
                                                                </div>
                                                                <div class="clear"></div>
                                                                <div class="gdlr-core-column-30">
                                                                    <span class="wpcf7-form-control-wrap your-email">
                                                                        <input type="email" name="email" value="" size="40" class="wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email" aria-required="true" aria-invalid="false" placeholder="Email*" required />
                                                                    </span>
                                                                </div>
                                                                <div class="gdlr-core-column-30">
                                                                    <span class="wpcf7-form-control-wrap your-phone">
                                                                        <input type="tel" name="phone" value="" size="40" class="wpcf7-form-control wpcf7-text wpcf7-tel wpcf7-validates-as-required wpcf7-validates-as-tel" aria-required="true" aria-invalid="false" placeholder="Phone*" required />
                                                                    </span>
                                                                </div>
                                                                <div class="clear"></div>
                                                                <div class="gdlr-core-column-60">
                                                                    <span class="wpcf7-form-control-wrap your-message">
                                                                        <textarea name="message" cols="40" rows="10" class="wpcf7-form-control wpcf7-textarea" aria-invalid="false" placeholder="Message"></textarea>
                                                                    </span>
                                                                </div>
                                                                <div class="gdlr-core-column-60 gdlr-core-left-align">
                                                                    <input type="submit" value="Submit Now" class="wpcf7-form-control has-spinner wpcf7-submit gdlr-core-large" />
                                                                </div>
                                                            </div>
                                                        </form>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script type="text/javascript" src="js/jquery.min.js?ver=3.6.0" id="jquery-core-js"></script>
    <script type="text/javascript" src="js/jquery-migrate.min.js?ver=3.3.2" id="jquery-migrate-js"></script>
    <script type="text/javascript" src="js/plugins/goodlayers-core/plugins/script.js" id="gdlr-core-plugin-js"></script>
    <script type="text/javascript" src="js/plugins/goodlayers-core/include/js/page-builder.js?ver=1.3.9" id="gdlr-core-page-builder-js"></script>
</body>
</html>
(function ($) {
    "use strict";
    /*=================================
        JS Index Here
    ==================================*/
    /*
    01. On Load Function
    02. Preloader
    03. Mobile Menu
    04. Sticky fix
    05. Scroll To Top
    06. Set Background Image Color & Mask
    07. Global Slider
    08. Ajax Contact Form
    09. Search Box Popup
    10. Popup Sidemenu
    11. Magnific Popup
    12. Section Position
    13. Filter
    14. Counter Up
    15. Shape Mockup
    16. Progress Bar Animation
    17. Countdown
    18. Image to SVG Code
    19. Tilt Active
    21. Service Active
    22. Circle Progress
    23. Scroll to the About section 
    24. Custom testimonials Slider 
    00. Woocommerce Toggle
    00. Right Click Disable
    */
    /*=================================
        JS Index End
    ==================================*/
    /*

  /*---------- 01. On Load Function ----------*/
  $(window).on("load", function () {
        $(".preloader").fadeOut();
        wowAnimation();
    });
    
     // $('select').niceSelect();
     if ($(".nice-select").length) {
        $(".nice-select").niceSelect();
    }


    /*---------- 02. Preloader ----------*/
    if ($(".preloader").length > 0) {
        $(".preloaderCls").each(function () {
            $(this).on("click", function (e) {
                e.preventDefault();
                $(".preloader").css("display", "none");
            });
        });
    }

    /*---------- 03. Mobile Menu ----------*/
    $.fn.thmobilemenu = function (options) {
        var opt = $.extend(
            {
                menuToggleBtn: ".th-menu-toggle",
                bodyToggleClass: "th-body-visible",
                subMenuClass: "th-submenu",
                subMenuParent: "menu-item-has-children",
                thSubMenuParent: "th-item-has-children",
                subMenuParentToggle: "th-active",
                meanExpandClass: "th-mean-expand",
                appendElement: '<span class="th-mean-expand"></span>',
                subMenuToggleClass: "th-open",
                toggleSpeed: 400,
            },
            options
        );

        return this.each(function () {
            var menu = $(this); // Select menu

            // Menu Show & Hide
            function menuToggle() {
                menu.toggleClass(opt.bodyToggleClass);

                // collapse submenu on menu hide or show
                var subMenu = "." + opt.subMenuClass;
                $(subMenu).each(function () {
                    if ($(this).hasClass(opt.subMenuToggleClass)) {
                        $(this).removeClass(opt.subMenuToggleClass);
                        $(this).css("display", "none");
                        $(this).parent().removeClass(opt.subMenuParentToggle);
                    }
                });
            }

            // Class Set Up for every submenu
            menu.find("." + opt.subMenuParent).each(function () {
                var submenu = $(this).find("ul");
                submenu.addClass(opt.subMenuClass);
                submenu.css("display", "none");
                $(this).addClass(opt.subMenuParent);
                $(this).addClass(opt.thSubMenuParent); // Add th-item-has-children class
                $(this).children("a").append(opt.appendElement);
            });

            // Toggle Submenu
            function toggleDropDown($element) {
                var submenu = $element.children("ul");
                if (submenu.length > 0) {
                    $element.toggleClass(opt.subMenuParentToggle);
                    submenu.slideToggle(opt.toggleSpeed);
                    submenu.toggleClass(opt.subMenuToggleClass);
                }
            }

            // Submenu toggle Button
            var itemHasChildren = "." + opt.thSubMenuParent + " > a";
            $(itemHasChildren).each(function () {
                $(this).on("click", function (e) {
                    e.preventDefault();
                    toggleDropDown($(this).parent());
                });
            });

            // Menu Show & Hide On Toggle Btn click
            $(opt.menuToggleBtn).each(function () {
                $(this).on("click", function () {
                    menuToggle();
                });
            });

            // Hide Menu On outside click
            menu.on("click", function (e) {
                e.stopPropagation();
                menuToggle();
            });

            // Stop Hide full menu on menu click
            menu.find("div").on("click", function (e) {
                e.stopPropagation();
            });
        });
    };

    $(".th-menu-wrapper").thmobilemenu();

    /*----------- 3. One Page Nav ----------*/
    function onePageNav(element) {
        if ($(element).length > 0) {
            $(element).each(function () {
                var link = $(this).find('a');
                $(this).find(link).each(function () {
                    $(this).on('click', function () {
                        var target = $(this.getAttribute('href'));
                        if (target.length) {
                            event.preventDefault();
                            $('html, body').stop().animate({
                                scrollTop: target.offset().top - 10
                            }, 1000);
                        };

                    });
                });
            })
        }
    };
    onePageNav('.onepage-nav');
    onePageNav('.scroll-down');
    //one page sticky menu  
    $(window).on('scroll', function () {
        if ($('.onepage-nav').length > 0) {};
    });
    

    /*---------- 04. Sticky fix ----------*/
    $(window).scroll(function () {
        var topPos = $(this).scrollTop();
        if (topPos > 500) {
            $(".sticky-wrapper").addClass("sticky");
            $(".category-menu").addClass("close-category");
        } else {
            $(".sticky-wrapper").removeClass("sticky");
            $(".category-menu").removeClass("close-category");
        }
    });


    /*---------- Wow Active ----------*/
    function wowAnimation() {
        var wow = new WOW({
            boxClass: 'wow',
            animateClass: 'animated',
            offset: 0,
            mobile: false,
            live: true
        });
        wow.init();
    }
    
    $(".menu-expand").each(function () {
        $(this).on("click", function (e) {
            e.preventDefault();
            $(".category-menu").toggleClass("open-category");
        });
    });

    /*---------- 05. Scroll To Top ----------*/
    if ($(".scroll-top").length > 0) {
        var scrollTopbtn = document.querySelector(".scroll-top");
        var progressPath = document.querySelector(".scroll-top path");
        var pathLength = progressPath.getTotalLength();
        progressPath.style.transition = progressPath.style.WebkitTransition =
            "none";
        progressPath.style.strokeDasharray = pathLength + " " + pathLength;
        progressPath.style.strokeDashoffset = pathLength;
        progressPath.getBoundingClientRect();
        progressPath.style.transition = progressPath.style.WebkitTransition =
            "stroke-dashoffset 10ms linear";
        var updateProgress = function () {
            var scroll = $(window).scrollTop();
            var height = $(document).height() - $(window).height();
            var progress = pathLength - (scroll * pathLength) / height;
            progressPath.style.strokeDashoffset = progress;
        };
        updateProgress();
        $(window).scroll(updateProgress);
        var offset = 50;
        var duration = 750;
        jQuery(window).on("scroll", function () {
            if (jQuery(this).scrollTop() > offset) {
                jQuery(scrollTopbtn).addClass("show");
            } else {
                jQuery(scrollTopbtn).removeClass("show");
            }
        });
        jQuery(scrollTopbtn).on("click", function (event) {
            event.preventDefault();
            jQuery("html, body").animate({ scrollTop: 0 }, duration);
            return false;
        });
    }

    /*---------- 06. Set Background Image Color & Mask ----------*/
    if ($("[data-bg-src]").length > 0) {
        $("[data-bg-src]").each(function () {
            var src = $(this).attr("data-bg-src");
            $(this).css("background-image", "url(" + src + ")");
            $(this).removeAttr("data-bg-src").addClass("background-image");
        });
    }

    if ($("[data-bg-color]").length > 0) {
        $("[data-bg-color]").each(function () {
            var color = $(this).attr("data-bg-color");
            $(this).css("background-color", color);
            $(this).removeAttr("data-bg-color");
        });
    }

    if ($("[data-theme-color]").length > 0) {
        $("[data-theme-color]").each(function () {
            var $color = $(this).attr("data-theme-color");
            $(this).get(0).style.setProperty("--theme-color", $color);
            $(this).removeAttr("data-theme-color");
        });
    }

    $("[data-border]").each(function () {
        var borderColor = $(this).data("border");
        $(this).css("--th-border-color", borderColor);
    });

    if ($("[data-mask-src]").length > 0) {
        $("[data-mask-src]").each(function () {
            var mask = $(this).attr("data-mask-src");
            $(this).css({
                "mask-image": "url(" + mask + ")",
                "-webkit-mask-image": "url(" + mask + ")",
            });
            $(this).addClass("bg-mask");
            $(this).removeAttr("data-mask-src");
        });
    }

    /*----------- 07. Global Slider ----------*/
    $(".th-slider").each(function () {
        var thSlider = $(this);
        var settings = $(this).data("slider-options");

        // Store references to navigation and pagination elements
        var prevArrow = thSlider.find(".slider-prev");
        var nextArrow = thSlider.find(".slider-next");
        var paginationEl1 = thSlider.find(".slider-pagination").get(0);
        var paginationEl2 = thSlider.find(".slider-pagination2").get(0); // Second pagination element

        var paginationType = settings["paginationType"] || "bullets";
        var autoplayCondition = settings['autoplay']

        var sliderDefault = {
            slidesPerView: 1,
            spaceBetween: settings["spaceBetween"] || 24,
            loop: settings["loop"] !== false,
            speed: settings["speed"] || 1000,
            autoplay: autoplayCondition || { delay: 6000, disableOnInteraction: false },
            navigation: {
                nextEl: nextArrow.get(0),
                prevEl: prevArrow.get(0),
            },
            pagination: {
                el: paginationEl1,
                type: paginationType,
                clickable: true,
                renderBullet: function (index, className) {
                    var number = index + 1;
                    var formattedNumber = number < 10 ? "0" + number : number;
                    return (
                        '<span class="' +
                        className +
                        '" aria-label="Go to Slide ' +
                        formattedNumber +
                        '"></span>'
                    );
                },
            },
            on: {
                init: function () {
                    // Calculate the total number of real slides (excluding duplicates)
                    var totalSlides = this.el.querySelectorAll('.swiper-slide:not(.swiper-slide-duplicate)').length;

                    // Initialize pagination for .slider-pagination2
                    if (paginationEl2) {
                        $(paginationEl2).html(
                            '<span class="current-slide">01</span> <span class="total-slides">' +
                            (totalSlides < 10 ? "0" + totalSlides : totalSlides) +
                            "</span>"
                        );
                    }
                },
                slideChange: function () {
                    var realIndex = this.realIndex + 1; // +1 for 1-based index
                    var totalSlides = this.el.querySelectorAll('.swiper-slide:not(.swiper-slide-duplicate)').length;

                    // Update pagination for .slider-pagination2
                    if (paginationEl2) {
                        $(paginationEl2).html(
                            '<span class="current-slide">' +
                            (realIndex < 10 ? "0" + realIndex : realIndex) +
                            '</span> <span class="total-slides">' +
                            (totalSlides < 10 ? "0" + totalSlides : totalSlides) +
                            "</span>"
                        );
                    }
                },
            },
        };

        // Merge default settings with custom options
        var options = $.extend({}, sliderDefault, settings);
        var swiper = new Swiper(thSlider.get(0), options); // Initialize Swiper

            // Apply panorama effect to slides with images
            thSlider.find('.swiper-slide').each(function () {
                var slide = $(this);
                var image = slide.find('img');
    
                if (image.length) {
                    var panoramaImageSrc = image.attr('src');
                    var viewerContainer = slide.find('.explore-single-slide1, .propery-single-slide').get(0);
                    // var viewerContainer = slide.find('.explore-single-slide, .propery-single-slide').get(0);
    
                    if (viewerContainer) {
                        var panoramaImage = new PANOLENS.ImagePanorama(panoramaImageSrc);
                        var viewer = new PANOLENS.Viewer({
                            container: viewerContainer,
                            autoRotate: true,
                            autoRotateSpeed: 0.3,
                            controlBar: false,
                            enableZoom: true,
                        });
                        viewerContainer.addEventListener("wheel", function (event) {
                            event.preventDefault();
                        }, { passive: false });
                        viewer.add(panoramaImage);
    
                        // Disable Swiper interactions when viewing panorama
                        viewer.addEventListener('enter', function () {
                            swiperInstance.allowTouchMove = false;
                        });
                        viewer.addEventListener('exit', function () {
                            swiperInstance.allowTouchMove = true;
                        });
                        
                    }
                }
            });
            

        // Add a custom class for the arrow wrapper
        if ($(".slider-area").length > 0) {
            $(".slider-area").closest(".container").parent().addClass("arrow-wrap");
        }
    });


    /*----------- External Navigation for Sliders ----------*/
    $("[data-slider-prev], [data-slider-next]").on("click", function () {
        var sliderSelector = $(this).data("slider-prev") || $(this).data("slider-next");
        var targetSlider = $(sliderSelector);

        if (targetSlider.length) {
            var swiper = targetSlider[0].swiper;

            if (swiper) {
                if ($(this).data("slider-prev")) {
                    swiper.slidePrev();
                } else {
                    swiper.slideNext();
                }
            }
        }
    });

    /*----------- Ensure Swipers Work Inside Tabs ----------*/
    $("[data-bs-toggle='tab']").on("shown.bs.tab", function (e) {
        var targetTabContent = $($(e.target).attr("href"));
        var swiperContainer = targetTabContent.find(".swiper-container");

        swiperContainer.each(function () {
            var swiperInstance = this.swiper;
            if (swiperInstance) {
                swiperInstance.update(); // Update Swiper dimensions
            }
        });
    });
    
    // Function to add animation classes
    function animationProperties() {
        $("[data-ani]").each(function () {
            var animationName = $(this).data("ani");
            $(this).addClass(animationName);
        });
    
        $("[data-ani-delay]").each(function () {
            var delayTime = $(this).data("ani-delay");
            $(this).css("animation-delay", delayTime);
        });
    }
    animationProperties();

    /*--------------. Slider Tab -------------*/
    $.fn.activateSliderThumbs = function (options) {
        var opt = $.extend(
            {
                sliderTab: false,
                tabButton: ".tab-btn",
            },
            options
        );

        return this.each(function () {
            var $container = $(this);
            var $thumbs = $container.find(opt.tabButton);
            var $line = $('<span class="indicator"></span>').appendTo(
                $container
            );

            var sliderSelector = $container.data("slider-tab");
            var $slider = $(sliderSelector);

            var swiper = $slider[0].swiper;

            $thumbs.on("click", function (e) {
                e.preventDefault();
                var clickedThumb = $(this);

                clickedThumb
                    .addClass("active")
                    .siblings()
                    .removeClass("active");
                linePos(clickedThumb, $container);

                if (opt.sliderTab) {
                    var slideIndex = clickedThumb.index();
                    swiper.slideTo(slideIndex);
                }
            });

            if (opt.sliderTab) {
                swiper.on("slideChange", function () {
                    var activeIndex = swiper.realIndex;
                    var $activeThumb = $thumbs.eq(activeIndex);

                    $activeThumb
                        .addClass("active")
                        .siblings()
                        .removeClass("active");
                    linePos($activeThumb, $container);
                });

                var initialSlideIndex = swiper.activeIndex;
                var $initialThumb = $thumbs.eq(initialSlideIndex);
                $initialThumb
                    .addClass("active")
                    .siblings()
                    .removeClass("active");
                linePos($initialThumb, $container);
            }

            function linePos($activeThumb) {
                var thumbOffset = $activeThumb.position();

                var marginTop = parseInt($activeThumb.css("margin-top")) || 0;
                var marginLeft = parseInt($activeThumb.css("margin-left")) || 0;

                $line.css("--height-set", $activeThumb.outerHeight() + "px");
                $line.css("--width-set", $activeThumb.outerWidth() + "px");
                $line.css("--pos-y", thumbOffset.top + marginTop + "px");
                $line.css("--pos-x", thumbOffset.left + marginLeft + "px");
            }
        });
    };

    if ($(".testi-grid-dots").length) {
        $(".testi-grid-dots").activateSliderThumbs({
            sliderTab: true,
            tabButton: ".tab-btn",
        });
    }

    /*----------- 08. Ajax Contact Form ----------*/
    var form = ".ajax-contact";
    var invalidCls = "is-invalid";
    var $email = '[name="email"]';
    var $validation =
        '[name="name"],[name="email"],[name="subject"],[name="number"],[name="message"]'; // Must be use (,) without any space
    var formMessages = $(".form-messages");

    function sendContact() {
        var formData = $(form).serialize();
        var valid;
        valid = validateContact();
        if (valid) {
            jQuery
                .ajax({
                    url: $(form).attr("action"),
                    data: formData,
                    type: "POST",
                })
                .done(function (response) {
                    // Make sure that the formMessages div has the 'success' class.
                    formMessages.removeClass("error");
                    formMessages.addClass("success");
                    // Set the message text.
                    formMessages.text(response);
                    // Clear the form.
                    $(
                        form +
                            ' input:not([type="submit"]),' +
                            form +
                            " textarea"
                    ).val("");
                })
                .fail(function (data) {
                    // Make sure that the formMessages div has the 'error' class.
                    formMessages.removeClass("success");
                    formMessages.addClass("error");
                    // Set the message text.
                    if (data.responseText !== "") {
                        formMessages.html(data.responseText);
                    } else {
                        formMessages.html(
                            "Oops! An error occured and your message could not be sent."
                        );
                    }
                });
        }
    }

    function validateContact() {
        var valid = true;
        var formInput;

        function unvalid($validation) {
            $validation = $validation.split(",");
            for (var i = 0; i < $validation.length; i++) {
                formInput = form + " " + $validation[i];
                if (!$(formInput).val()) {
                    $(formInput).addClass(invalidCls);
                    valid = false;
                } else {
                    $(formInput).removeClass(invalidCls);
                    valid = true;
                }
            }
        }
        unvalid($validation);

        if (
            !$($email).val() ||
            !$($email)
                .val()
                .match(/^([\w-\.]+@([\w-]+\.)+[\w-]{2,4})?$/)
        ) {
            $($email).addClass(invalidCls);
            valid = false;
        } else {
            $($email).removeClass(invalidCls);
            valid = true;
        }
        return valid;
    }

    $(form).on("submit", function (element) {
        element.preventDefault();
        sendContact();
    });

    /*---------- 09. Search Box Popup ----------*/
    function popupSarchBox($searchBox, $searchOpen, $searchCls, $toggleCls) {
        $($searchOpen).on("click", function (e) {
            e.preventDefault();
            $($searchBox).addClass($toggleCls);
        });
        $($searchBox).on("click", function (e) {
            e.stopPropagation();
            $($searchBox).removeClass($toggleCls);
        });
        $($searchBox)
            .find("form")
            .on("click", function (e) {
                e.stopPropagation();
                $($searchBox).addClass($toggleCls);
            });
        $($searchCls).on("click", function (e) {
            e.preventDefault();
            e.stopPropagation();
            $($searchBox).removeClass($toggleCls);
        });
    }
    popupSarchBox(
        ".popup-search-box",
        ".searchBoxToggler",
        ".searchClose",
        "show"
    );

    /*---------- 10. Popup Sidemenu ----------*/
    function popupSideMenu($sideMenu, $sideMunuOpen, $sideMenuCls, $toggleCls) {
        // Sidebar Popup
        $($sideMunuOpen).on("click", function (e) {
            e.preventDefault();
            $($sideMenu).addClass($toggleCls);
        });
        $($sideMenu).on("click", function (e) {
            e.stopPropagation();
            $($sideMenu).removeClass($toggleCls);
        });
        var sideMenuChild = $sideMenu + " > div";
        $(sideMenuChild).on("click", function (e) {
            e.stopPropagation();
            $($sideMenu).addClass($toggleCls);
        });
        $($sideMenuCls).on("click", function (e) {
            e.preventDefault();
            e.stopPropagation();
            $($sideMenu).removeClass($toggleCls);
        });
    }
    popupSideMenu(".sidemenu-cart", ".sideMenuToggler", ".sideMenuCls", "show");
    popupSideMenu(".sidemenu-info", ".sideMenuInfo", ".sideMenuCls", "show");

    /*----------- 11. Magnific Popup ----------*/
    /* magnificPopup img view */
    $(".popup-image").magnificPopup({
        type: "image",
        mainClass: "mfp-zoom-in",
        removalDelay: 260,
        gallery: {
            enabled: true,
        },
    });

    $(document).ready(function() {
        $('.popular-popup-image').magnificPopup({
            type: 'image',
            gallery: {
                enabled: true 
            }
        });
    
        $('.popular-popup-gallery').click(function(e) {
            e.preventDefault();
    
            $('.popular-popup-image:first').click(); 
        });
    });


    /* magnificPopup video view */
    $(".popup-video").magnificPopup({
        type: "iframe",
    });

    /* magnificPopup video view */
    $(".popup-content").magnificPopup({
        type: "inline",
        midClick: true,
    });

    /*---------- 12. Section Position ----------*/
    // Interger Converter
    function convertInteger(str) {
        return parseInt(str, 10);
    }

    $.fn.sectionPosition = function (mainAttr, posAttr) {
        $(this).each(function () {
            var section = $(this);

            function setPosition() {
                var sectionHeight = Math.floor(section.height() / 2), // Main Height of section
                    posData = section.attr(mainAttr), // where to position
                    posFor = section.attr(posAttr), // On Which section is for positioning
                    topMark = "top-half", // Pos top
                    bottomMark = "bottom-half", // Pos Bottom
                    parentPT = convertInteger($(posFor).css("padding-top")), // Default Padding of  parent
                    parentPB = convertInteger($(posFor).css("padding-bottom")); // Default Padding of  parent

                if (posData === topMark) {
                    $(posFor).css(
                        "padding-bottom",
                        parentPB + sectionHeight + "px"
                    );
                    section.css("margin-top", "-" + sectionHeight + "px");
                } else if (posData === bottomMark) {
                    $(posFor).css(
                        "padding-top",
                        parentPT + sectionHeight + "px"
                    );
                    section.css("margin-bottom", "-" + sectionHeight + "px");
                }
            }
            setPosition(); // Set Padding On Load
        });
    };

    var postionHandler = "[data-sec-pos]";
    if ($(postionHandler).length) {
        $(postionHandler).imagesLoaded(function () {
            $(postionHandler).sectionPosition("data-sec-pos", "data-pos-for");
        });
    }

    /*----------- 14. Filter ----------*/
    $(".filter-active").imagesLoaded(function () {
        var $filter = ".filter-active",
            $filterItem = ".filter-item",
            $filterMenu = ".filter-menu-active";

        if ($($filter).length > 0) {
            var $grid = $($filter).isotope({
                itemSelector: $filterItem,
                filter: "*",
                masonry: {
                    // use outer width of grid-sizer for columnWidth
                    // columnWidth: 1,
                },
            });

            // filter items on button click
            $($filterMenu).on("click", "button", function () {
                var filterValue = $(this).attr("data-filter");
                $grid.isotope({
                    filter: filterValue,
                });
            });

            // Menu Active Class
            $($filterMenu).on("click", "button", function (event) {
                event.preventDefault();
                $(this).addClass("active");
                $(this).siblings(".active").removeClass("active");
            });
        }
    });

    $(".masonary-active, .woocommerce-Reviews .comment-list").imagesLoaded(
        function () {
            var $filter =
                    ".masonary-active, .woocommerce-Reviews .comment-list",
                $filterItem =
                    ".filter-item, .woocommerce-Reviews .comment-list li";

            if ($($filter).length > 0) {
                $($filter).isotope({
                    itemSelector: $filterItem,
                    filter: "*",
                    masonry: {
                        // use outer width of grid-sizer for columnWidth
                        columnWidth: 1,
                    },
                });
            }
            $('[data-bs-toggle="tab"]').on("shown.bs.tab", function (e) {
                $($filter).isotope({
                    filter: "*",
                });
            });
        }
    );

    /*----------- 22. Indicator ----------*/
    // Indicator
    $.fn.indicator = function () {
        // Loop through each .indicator-active element
        $(this).each(function () {
            var $menu = $(this),
                $linkBtn = $menu.find("a"),
                $btn = $menu.find("button");

            // Append indicator
            $menu.append('<span class="indicator"></span>');
            var $line = $menu.find(".indicator");

            // Check which type button is Available
            var $currentBtn;
            if ($linkBtn.length) {
                $currentBtn = $linkBtn;
            } else if ($btn.length) {
                $currentBtn = $btn;
            }

            // On Click Button Class Remove
            $currentBtn.on("click", function (e) {
                e.preventDefault();
                $(this).addClass("active");
                $(this).siblings(".active").removeClass("active");
                linePos();
            });

            // Indicator Position
            function linePos() {
                var $btnActive = $menu.find(".active"),
                    $height = $btnActive.css("height"),
                    $width = $btnActive.css("width"),
                    $top = $btnActive.position().top + "px",
                    $left = $btnActive.position().left + "px";

                $(window).on("resize", function () {
                    ($top = $btnActive.position().top + "px"),
                        ($left = $btnActive.position().left + "px");
                });

                $line.get(0).style.setProperty("--height-set", $height);
                $line.get(0).style.setProperty("--width-set", $width);
                $line.get(0).style.setProperty("--pos-y", $top);
                $line.get(0).style.setProperty("--pos-x", $left);
            }

            linePos();
            $(window).on("resize", function () {
                linePos();
            });
        });
    };

    if ($(".indicator-active").length) {
        $(".indicator-active").indicator();
    }

    /************lettering js***********/
    function injector(t, splitter, klass, after) {
        var a = t.text().split(splitter),
            inject = "";
        if (a.length) {
            $(a).each(function (i, item) {
                inject +=
                    '<span class="' +
                    klass +
                    (i + 1) +
                    '">' +
                    item +
                    "</span>" +
                    after;
            });
            t.empty().append(inject);
        }
    }

    var methods = {
        init: function () {
            return this.each(function () {
                injector($(this), "", "char", "");
            });
        },

        words: function () {
            return this.each(function () {
                injector($(this), " ", "word", " ");
            });
        },

        lines: function () {
            return this.each(function () {
                var r = "eefec303079ad17405c889e092e105b0";
                // Because it's hard to split a <br/> tag consistently across browsers,
                // (*ahem* IE *ahem*), we replaces all <br/> instances with an md5 hash
                // (of the word "split").  If you're trying to use this plugin on that
                // md5 hash string, it will fail because you're being ridiculous.
                injector(
                    $(this).children("br").replaceWith(r).end(),
                    r,
                    "line",
                    ""
                );
            });
        },
    };

    $.fn.lettering = function (method) {
        // Method calling logic
        if (method && methods[method]) {
            return methods[method].apply(this, [].slice.call(arguments, 1));
        } else if (method === "letters" || !method) {
            return methods.init.apply(this, [].slice.call(arguments, 0)); // always pass an array
        }
        $.error("Method " + method + " does not exist on jQuery.lettering");
        return this;
    };

    $(".logo-animation").lettering();

    /*----------- 14. Counter Up ----------*/
    $(".counter-number").counterUp({
        delay: 10,
        time: 1000,
    });

    /*----------- 15. Shape Mockup ----------*/
    $.fn.shapeMockup = function () {
        var $shape = $(this);
        $shape.each(function () {
            var $currentShape = $(this),
                shapeTop = $currentShape.data("top"),
                shapeRight = $currentShape.data("right"),
                shapeBottom = $currentShape.data("bottom"),
                shapeLeft = $currentShape.data("left");
            $currentShape
                .css({
                    top: shapeTop,
                    right: shapeRight,
                    bottom: shapeBottom,
                    left: shapeLeft,
                })
                .removeAttr("data-top")
                .removeAttr("data-right")
                .removeAttr("data-bottom")
                .removeAttr("data-left")
                .parent()
                .addClass("shape-mockup-wrap");
        });
    };

    if ($(".shape-mockup")) {
        $(".shape-mockup").shapeMockup();
    }

    /*----------- 16. Progress Bar Animation ----------*/
    $(".progress-bar").waypoint(
        function () {
            $(".progress-bar").css({
                animation: "animate-positive 1.8s",
                opacity: "1",
            });
        },
        { offset: "100%" }
    );

    /*----------- 17. Countdown ----------*/
    $.fn.countdown = function () {
        $(this).each(function () {
            var $counter = $(this),
                countDownDate = new Date($counter.data("offer-date")).getTime(), // Set the date we're counting down toz
                exprireCls = "expired";

            // Finding Function
            function s$(element) {
                return $counter.find(element);
            }

            // Update the count down every 1 second
            var counter = setInterval(function () {
                // Get today's date and time
                var now = new Date().getTime();

                // Find the distance between now and the count down date
                var distance = countDownDate - now;

                // Time calculations for days, hours, minutes and seconds
                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor(
                    (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
                );
                var minutes = Math.floor(
                    (distance % (1000 * 60 * 60)) / (1000 * 60)
                );
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                // Check If value is lower than ten, so add zero before number
                days < 10 ? (days = "0" + days) : null;
                hours < 10 ? (hours = "0" + hours) : null;
                minutes < 10 ? (minutes = "0" + minutes) : null;
                seconds < 10 ? (seconds = "0" + seconds) : null;

                // If the count down is over, write some text
                if (distance < 0) {
                    clearInterval(counter);
                    $counter.addClass(exprireCls);
                    $counter.find(".message").css("display", "block");
                } else {
                    // Output the result in elements
                    s$(".day").html(days);
                    s$(".hour").html(hours);
                    s$(".minute").html(minutes);
                    s$(".seconds").html(seconds);
                }
            }, 1000);
        });
    };

    if ($(".counter-list").length) {
        $(".counter-list").countdown();
    }

    /*---------- 18. Image to SVG Code ----------*/
    const cache = {};

    $.fn.inlineSvg = function fnInlineSvg() {
        this.each(imgToSvg);

        return this;
    };

    function imgToSvg() {
        const $img = $(this);
        const src = $img.attr("src");

        // fill cache by src with promise
        if (!cache[src]) {
            const d = $.Deferred();
            $.get(src, (data) => {
                d.resolve($(data).find("svg"));
            });
            cache[src] = d.promise();
        }

        // replace img with svg when cached promise resolves
        cache[src].then((svg) => {
            const $svg = $(svg).clone();

            if ($img.attr("id")) $svg.attr("id", $img.attr("id"));
            if ($img.attr("class")) $svg.attr("class", $img.attr("class"));
            if ($img.attr("style")) $svg.attr("style", $img.attr("style"));

            if ($img.attr("width")) {
                $svg.attr("width", $img.attr("width"));
                if (!$img.attr("height")) $svg.removeAttr("height");
            }
            if ($img.attr("height")) {
                $svg.attr("height", $img.attr("height"));
                if (!$img.attr("width")) $svg.removeAttr("width");
            }

            $svg.insertAfter($img);
            $img.trigger("svgInlined", $svg[0]);
            $img.remove();
        });
    }

    $(".svg-img").inlineSvg();

    /*----------- 20. Color Scheme ----------*/
    $(".color-switch-btns button").each(function () {
        // Get color for button
        const button = $(this);
        const color = button.data("color");
        button.css("--theme-color", color);

        // Change theme color on click
        button.on("click", function () {
            const clickedColor = $(this).data("color");
            $(":root").css("--theme-color", clickedColor);
        });
    });

    // Handle color picker change event
    $("#thcolorpicker").on("input", function () {
        const pickedColor = $(this).val();
        updateThemeColor(pickedColor);
    });

    function updateThemeColor(color) {
        $(":root").css("--theme-color", color);
    }

    $(document).on("click", ".switchIcon", function () {
        $(".color-scheme").toggleClass("active");
    });

    /*----------- 19. Tilt Active ----------*/

    $(".tilt-active").tilt({
        maxTilt: 7,
        perspective: 1000,
    });

    /*----------- 21. Service Active ----------*/
    $(".service-3-item").on("mouseenter", function () {
        $(".service-3-item").removeClass("active");
        $(this).addClass("active");
    });

    $(".accordion-bottom__item").on("click", function () {
        $(".accordion-bottom__item").removeClass("active");
        $(this).addClass("active");
    });

    /*---------- 22. Circle Progress ----------*/

    document.addEventListener("DOMContentLoaded", function () {
        const progressBars = document.querySelectorAll(".circular-progress");

        progressBars.forEach((progressBar) => {
            const circle = progressBar.querySelector(".circle");
            const percentageDisplay = progressBar.querySelector(".percentage");
            const target = parseInt(
                progressBar.getAttribute("data-target"),
                10
            );
            let progressValue = 0;

            const animateProgress = () => {
                if (progressValue <= target) {
                    const offset = 100 - (progressValue * 100) / 100;
                    circle.style.strokeDashoffset = offset;
                    percentageDisplay.textContent = progressValue + "%";
                    progressValue++;
                    requestAnimationFrame(animateProgress);
                }
            };

            animateProgress();
        });
    });

    /*----------- 23. Scroll to the About section ----------*/
    $("#scroll-about-sec").on("click", function () {
        $("html, body").animate(
            {
                scrollTop: $("#about-sec").offset().top,
            },
            800
        ); // 800ms for smooth scrolling
    });

    /*-------------- 24 Custom testimonials Slider -------------*/
    $(".service-list-wrap").on("click", function () {
        $(this).addClass("active").siblings().removeClass("active");
    });
    function showNextService() {
        var $activeService = $(".service-list-area .service-list-wrap.active");
        if ($activeService.next().length > 0) {
            $activeService.removeClass("active");
            $activeService.next().addClass("active");
        } else {
            $activeService.removeClass("active");
            $(".service-list-area .service-list-wrap:first").addClass("active");
        }
    }

    function showPreviousService() {
        var $activeService = $(".service-list-area .service-list-wrap.active");
        if ($activeService.prev().length > 0) {
            $activeService.removeClass("active");
            $activeService.prev().addClass("active");
        } else {
            $activeService.removeClass("active");
            $(".service-list-area .service-list-wrap:last").addClass("active");
        }
    }
    $(".service-prev").on("click", function () {
        showPreviousService();
    });
    $(".service-next").on("click", function () {
        showNextService();
    });

    /*-----------  Price Slider ----------*/
    $(".price_slider").slider({
        range: true,
        min: 125000,
        max: 825000,
        values: [125000, 825000],
        slide: function (event, ui) {
            $(".from").text("$" + ui.values[0]);
            $(".to").text("$" + ui.values[1]);
        },
    });
    $(".from").text("$" + $(".price_slider").slider("values", 0));
    $(".to").text("$" + $(".price_slider").slider("values", 1));

    /**----- Gallery Active class -----*/
    $(".single-inventory-item").on("mouseenter", function () {
        $(".single-inventory-item").removeClass("active"); 
        $(this).addClass("active");
    });
    
    /*----------- 00. Woocommerce Toggle ----------*/
    // Ship To Different Address
    $("#ship-to-different-address-checkbox").on("change", function () {
        if ($(this).is(":checked")) {
            $("#ship-to-different-address")
                .next(".shipping_address")
                .slideDown();
        } else {
            $("#ship-to-different-address").next(".shipping_address").slideUp();
        }
    });

    // Login Toggle
    $(".woocommerce-form-login-toggle a").on("click", function (e) {
        e.preventDefault();
        $(".woocommerce-form-login").slideToggle();
    });

    // Coupon Toggle
    $(".woocommerce-form-coupon-toggle a").on("click", function (e) {
        e.preventDefault();
        $(".woocommerce-form-coupon").slideToggle();
    });

    // Woocommerce Shipping Method
    $(".shipping-calculator-button").on("click", function (e) {
        e.preventDefault();
        $(this).next(".shipping-calculator-form").slideToggle();
    });

    // Woocommerce Payment Toggle
    $('.wc_payment_methods input[type="radio"]:checked')
        .siblings(".payment_box")
        .show();
    $('.wc_payment_methods input[type="radio"]').each(function () {
        $(this).on("change", function () {
            $(".payment_box").slideUp();
            $(this).siblings(".payment_box").slideDown();
        });
    });

    // Woocommerce Rating Toggle
    $(".rating-select .stars a").each(function () {
        $(this).on("click", function (e) {
            e.preventDefault();
            $(this).siblings().removeClass("active");
            $(this).parent().parent().addClass("selected");
            $(this).addClass("active");
        });
    });

    // Quantity Plus Minus ---------------------------

    $(".quantity-plus").each(function () {
        $(this).on("click", function (e) {
            e.preventDefault();
            var $qty = $(this).siblings(".qty-input");
            var currentVal = parseInt($qty.val(), 10);
            if (!isNaN(currentVal)) {
                $qty.val(currentVal + 1);
            }
        });
    });

    $(".quantity-minus").each(function () {
        $(this).on("click", function (e) {
            e.preventDefault();
            var $qty = $(this).siblings(".qty-input");
            var currentVal = parseInt($qty.val(), 10);
            if (!isNaN(currentVal) && currentVal > 1) {
                $qty.val(currentVal - 1);
            }
        });
    });

    // Hero Search box  ---------------------------

    $(".advance-search-active").click(function(event){
        event.stopPropagation(); // Prevent event bubbling
        $(this).toggleClass("active");

        let searchWrapper = $(".advance-search-wrapper");
        let icon = $(this).find("i");

        if (searchWrapper.hasClass("open")) {
            // Close without animation
            searchWrapper.removeClass("open").hide();
            icon.removeClass("fa-times").addClass("fa-sliders-up");
        } else {
            // Open without animation
            searchWrapper.addClass("open").show();
            icon.removeClass("fa-sliders-up").addClass("fa-times");
        }
    });

    // Click outside to close, but ignore clicks inside .select-group-wrapper
    $(document).click(function(event) {
        if (!$(event.target).closest(".advance-search-wrapper, .advance-search-active, .select-group-wrapper").length) {
            $(".advance-search-wrapper").removeClass("open").hide();
            $(".advance-search-active").removeClass("active");
            $(".advance-search-active i").removeClass("fa-times").addClass("fa-sliders-up");
        }
    });


    document.addEventListener("DOMContentLoaded", function () {
        const hotspotDots = document.querySelectorAll(".map-icon");
        const productHotspotDots = document.querySelectorAll(".map-popular-list");
    
        let activeIndex = null; // Track the active hotspot index
    
        hotspotDots.forEach((dot, index) => {
            dot.addEventListener("mouseenter", function () {
                // Hide all product hotspot dots
                productHotspotDots.forEach(dot => dot.classList.remove("show"));
    
                // Show the corresponding map-popular-list
                const productDot = document.querySelector(`.map-popular-list${index + 1}`);
                productDot.classList.add("show");
    
                // Update the active index
                activeIndex = index + 1;
            });
        });
    
        productHotspotDots.forEach((productDot) => {
            productDot.addEventListener("mouseenter", function () {
                this.classList.add("show");
            });
    
            productDot.addEventListener("mouseleave", function () {
                this.classList.remove("show"); // Hide when mouse leaves
            });
        });
    
        // Click anywhere outside to hide all map-popular-list elements
        document.addEventListener("click", function (event) {
            if (!event.target.closest(".map-icon") && !event.target.closest(".map-popular-list")) {
                productHotspotDots.forEach(dot => dot.classList.remove("show"));
            }
        });
    });
    

    $(document).ready(function () {
        $(".add-explore-city-icon").on("mouseenter", function () {
          $(this).next(".explore-card").addClass("active");
        });
      
        $(".add-explore-city-icon, .explore-card").on("mouseleave", function (e) {
          // Check korbo mouse ki explore-card or icon er baire chole geche
          if (!$(e.relatedTarget).closest('.add-explore-city-icon, .explore-card').length) {
            $(".explore-card").removeClass("active");
          }
        });
      });
      

    // /*----------- 00. Right Click Disable ----------*/
    //   window.addEventListener('contextmenu', function (e) {
    //     // do something here...
    //     e.preventDefault();
    //   }, false);

    // /*----------- 00. Inspect Element Disable ----------*/
    //   document.onkeydown = function (e) {
    //     if (event.keyCode == 123) {
    //       return false;
    //     }
    //     if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
    //       return false;
    //     }
    //     if (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) {
    //       return false;
    //     }
    //     if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
    //       return false;
    //     }
    //     if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
    //       return false;
    //     }
    //   }
})(jQuery);

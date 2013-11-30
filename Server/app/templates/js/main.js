/* ================================================
----------- Kira Main javascript file ---------- */
(function ($) {
	"use strict";

/* tooltip */
	$('.add-tooltip').tooltip();

/* Select nav plugin */
	selectnav('nav');

/* =========================================
---- Triangle border width
=========================================== */
	var setBorderWidth = function () {
		var parent = $('.triangle-border').parent();
		if (!parent) {
			parent = $(window);
		}
    
		var parentWidth = parent.width();
    
		$('.triangle-top-left, .triangle-bottom-left').css({'border-left-width' : parentWidth});
		$('.triangle-top-right, .triangle-bottom-right').css({'border-right-width' : parentWidth});

	};
	setBorderWidth();

	$(window).on('resize', setBorderWidth);


/* =========================================
---- Check for placholder support 
---- if its not suppoerted active plugin
=========================================== */
	function placeholderIsSupported() {
		var test = document.createElement('input');
		return ('placeholder' in test);
	}

/* if placeholder not supported  use placeholder plugin */
	if (!placeholderIsSupported()) {
		$('input, textarea').placeholder();
	}


/* =========================================
---- Responsive video / fitvids plugin
=========================================== */
	$(".video-container").fitVids();


/* =========================================
---- CountTo plugin
=========================================== */
	if ($.fn.countTo) {
		$('.count').countTo();
    
    /* after appear event call again */
		$('.appear-count').appear();
		$('.appear-count').on('appear', function (e, i) {
			if (!$(this).hasClass('activated')) {
				$('.count').countTo();
				$(this).addClass('activated');
			}
		});
	}


/* =========================================
---- Menu Sticky
=========================================== */

	$(window).on('scroll', function () {
		var windowTop = $(window).scrollTop(),
			header = $('#header'),
			headerHeight = header.height();
		if (windowTop > headerHeight) {
			header.addClass('fixed');
		} else {
			header.removeClass('fixed');
		}
    
	});

/* =========================================
---- ScrollTop Button / Animation
=========================================== */
	$(window).on('scroll', function () {
		var windowTop = $(window).scrollTop(),
			scrollTop = $('#scroll-top');
        
        if (windowTop >= 300) {
            scrollTop.addClass('fixed');
        } else {
            scrollTop.removeClass('fixed');
        }
        
	});


	$('#scroll-top').on('click', function () {
		$('html, body').animate({ 'scrollTop' : 0 }, 1200);
	});


/* =========================================
---- Bootstrap.js tab 
=========================================== */
	// Elements.html
	$('#mytab a').on('click', function (e) {
		e.preventDefault();
		$(this).tab('show');
	});


/* =========================================
---- Appear Plugin
=========================================== */

/* progress bar */
	$('.appear-progress').appear();
	$('.appear-progress').on('appear', function (e, i) {
		var dataWidth = $(this).data('width');
		$(this).find('.progress-bar').css({ width : dataWidth + '%' });
	});

/* general
Just add appear class to element width data-appear-class="fadeInDown"  like so
When Element is visible you'll see the animation
fadeInDown or just pick a class name from animate-custom.css file for awesome animations while scrollin
*/
	$('.appear').appear();
	$('.appear').on('appear', function (e, i) {
		var appearClass = $(this).data('appear-class');
		$(this).css('visibility', 'visible').addClass('animated ' + appearClass);
	});


/* =========================================
---- carouFredSel Plugin
=========================================== */
	var customersCarou = $(".customers");
// if class exist
	if (customersCarou.length) {
		customersCarou.carouFredSel({
			items: {
				width       : 220,
				visible     : {
					min         : 1,
					max         : 5
				}
			},
			responsive  : true,
			direction: "left",
			scroll: {
				items: 1,
				easing: "quadratic",
				duration: 1400,
				pauseOnHover: true
			},
			prev: {
				button: "#customers-prev",
				key: "left"
			},
			next: {
				button: "#customers-next",
				key: "right"
			},
			debug: false
		});
	}

/* index latest project carousel */
	var latestProjectsCarou = $('#latest-projects');
// if exist

	if (latestProjectsCarou.length) {
		latestProjectsCarou.carouFredSel({
			width: '100%',
			items: {
				width: 252,
				visible: {
					min         : 1,
					max         : 3
				}
			},
			responsive  : true,
			direction: "left",
			scroll: {
				items: 1,
				duration: 1000,
				pauseOnHover: false
			},
			prev: {
				button: "#latest-projects-prev",
				key: "left"
			},
			next: {
				button: "#latest-projects-next",
				key: "right"
			},
			debug: false
		});
	}


/* index latest posts carousel */
	var latestPostsCarou = $('#latest-posts');
// if exist

	if (latestPostsCarou.length) {
		latestPostsCarou.carouFredSel({
			width: '100%',
			items: {
				width: 252,
				visible: {
					min: 1,
					max: 3
				}
			},
			responsive: true,
			direction: "left",
			scroll: {
				items: 1,
				duration: 1200,
				pauseOnHover: false
			},
			prev: {
				button: "#latest-posts-prev",
				key: "left"
			},
			next: {
				button: "#latest-posts-next",
				key: "right"
			},
			debug: false
		});
	}


/* =========================================
---- // // PrettyPhoto plugin 
// if not mobile, prettyphoto ( this plugin is not responsive )plugin will be activated
=========================================== */

	if ($.fn.prettyPhoto) {
		$("a[data-rel^='prettyPhoto']").prettyPhoto({
			hook: 'data-rel',
			animation_speed: 'fast',
			slideshow: 3000,
			autoplay_slideshow: false,
			show_title: false,
			deeplinking: false,
			social_tools: '',
			overlay_gallery: false,
			theme : 'light_square'
		});
	}

	
	$('.block-services, .block-services-border, .big-services').on('mouseover', function () {
		var $this = $(this);
		$this.find('.icon-container').addClass('animated fadeInDown');
		$this.find('h3').addClass('animated fadeInLeft');
		$this.find('p').addClass('animated fadeInUp');
	}).on('mouseleave', function () {
		var $this = $(this);
		$this.find('.icon-container').removeClass('animated fadeInDown');
		$this.find('h3').removeClass('animated fadeInLeft');
		$this.find('p').removeClass('animated fadeInUp');
	});

/* =========================================
---- Sharre plugin share buttons 
=========================================== */
	if ($.fn.sharrre) {
		$('#share').sharrre({
			share: {
				facebook: true,
				twitter: true,
				googlePlus: true
			},
			buttons: {
				googlePlus: {size: 'medium', annotation: 'bubble'},
				facebook: {layout: 'button_count'},
				twitter: {count: 'horizontal'}
			},
			enableHover: false,
			enableCounter: false,
			enableTracking: true
		});
	}


/*----------------------------------------------------*/
// Contact Form
/*----------------------------------------------------*/
	$('#contact-form').validate({
		rules: {
			contactname: 'required',
			contactemail: {
				required: true,
				email: true
			},
			contactsubject: 'required',
			contactmessage: {
				required: true,
				minlength: 50
			}
		},
		messages: {
			name: "This field is required. Please enter your name!",
			email: {
				required: "This field is required. Please enter your email!",
				email: "Please enter a valid email address!"
			},
			message: {
				required: "This field is required. Please enter your message!",
				minlength: "Your message must be at least 50 characters long!"
			}
		},
		submitHandler: function (form) {
				
					/* ajax request will be updated*/
					/* example ajax request
					$.ajax({
						type: 'post',
						url: '',
						data: $(form).serialize(),
					}).done(function( data ) {
						alert( data );
					}).error(function() {
						alert( 'There is an error please try later!' );
					});
					*/
			
			return false;
		}
	});



/* =========================================
---- Flickr plugin footer 
=========================================== */
	$('ul.flickr-widget').jflickrfeed({
		limit: 12,
		qstrings: {
			id: '52617155@N08'
		},
		itemTemplate:
			'<li>' +
				'<a data-rel="prettyPhoto" href="{{image}}" title="{{title}}">' +
					'<img src="{{image_s}}" alt="{{title}}" />' +
				'</a>' +
			'</li>'
	}, function () {
		if ($.fn.prettyPhoto) {
			/* update prettyphoto plugin for feeds */
			$("a[data-rel^='prettyPhoto']").prettyPhoto({
				hook: 'data-rel',
				animation_speed: 'fast',
				slideshow: 3000,
				autoplay_slideshow: false,
				show_title: false,
				deeplinking: false,
				social_tools: '',
				overlay_gallery: false,
				theme : 'light_square'
			});
		}
	   
	});


}(jQuery));


/*----------------------------------------------------*/
///* Google javascript api v3  -- map */
/*----------------------------------------------------*/
(function () {
	"use strict";
	
	function initialize() {
		/* change your with your coordinates */
		var myLatLng = new google.maps.LatLng(41.039193, 28.993818),
			mappy = {
				center: myLatLng,
				zoom: 15,
				scrollwheel: false,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
				styles: [{
					"elementType": "geometry",
					"stylers": [{
						"hue": "#000"
					}, {
						"weight": 1
					}, {
						"saturation": -250
					}, {
						"gamma": 0.73
					}, {
						"visibility": "on"
					}]
				}]
			};
		var map = new google.maps.Map(document.getElementById("map"), mappy);
	
		new google.maps.Marker({
			position: myLatLng,
			map: map,
			animation: google.maps.Animation.DROP,
			title: 'Hello from Gon'
		});
		}
		
	if (document.getElementById("map")) {
		google.maps.event.addDomListener(window, 'load', initialize);
	}

}());
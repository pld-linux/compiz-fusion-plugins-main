%define	pkgname	compiz-plugins-main
Summary:	Main Compiz Fusion plugins
Summary(pl.UTF-8):	Główne wtyczki Compiz Fusion
Name:		compiz-fusion-plugins-main
Version:	0.8.4
Release:	2
License:	GPL v2+
Group:		X11
Source0:	http://releases.compiz.org/%{version}/%{pkgname}-%{version}.tar.bz2
# Source0-md5:	7ac2b073d421a871b4d9f0741dde9164
URL:		http://www.compiz.org/
BuildRequires:	GConf2-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel >= 1.0
BuildRequires:	compiz-bcop >= %{version}
BuildRequires:	compiz-devel >= %{version}
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.10.0
BuildRequires:	pkgconfig
# GConf2-devel + compiz-gconf.pc to install schemas
Requires:	compiz >= %{version}
Obsoletes:	beryl-plugins
Obsoletes:	beryl-plugins-unsupported
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Animation: Animations for window open, close, minimize/restore, focus
    and shade events.
Colourfilter: Provides various filters to improve accessibility to
    vision impaired users.
Expo: Displays all viewports and allows the movement of a window from
    one viewport to another.
Enhanced Zoom (ezoom): Improved version of the Zoom plugin, featuring
    interaction with windows while zooming, plus several accessibility
    improvements such as focus tracking.
Jpeg: Adds JPEG images support to Compiz.
Neg: Shows negatives of windows.
Opacify: Reduce opacity of windows overlapping the window currently
    hovered over by the mouse pointer.
Put: Adds bindings to move windows to several positions.
Resizeinfo: Provides a small information window about the window
    dimensions during window resize.
Ring: An alternative application switcher plugin that arranges all
    windows in a ring.
Scaleaddon: Improves Compiz Scale plugin by displaying hovered windows
    titles or highlighting the currently selected window.
Shift: An alternative application switcher plugin that provides a 3D
    view of the switching process.
Snap: Adds snapping during window movement if the wobbly plugin is
    disabled.
Text: Offers pango-cairo based text rendering for different plugins.
Thumbnail: Shows a small thumbnail of a window if the mouse is over
    its entry in the taskbar.
Vpswitch: Uses mouse actions performed on the background to change the
    current viewport.
Wall: Arranges all viewports as a wall and features visual sliding
    between viewports as well as a preview window during switching.
Winrules: Enables setting of window properties by matching them by
    name, type, or other criteria.
Workarounds: Features several workarounds to improve behavior of
    legacy applications and such.

%description -l pl.UTF-8
Animation: Animacje zamykania, otwierania, minimalizacji okien.
Colourfilter: Pozwala użyć filtrów w celu zwiększenia dostępności
    użytkownikom z wadami wzroku.
Expo: Wyświetla wszystkie viewporty i umożliwia przesuwanie okien z
    jednego do drugiego.
Enhanced Zoom (ezoom): Rozszerzona wersja wtyczki Zoom, umożliwia
    interakcję z oknami podczas powiększenia, plus wiele udoskonaleń
    dostępności, jak na przykład śledzenie focusa.
Jpeg: Dodaje do Compiza obsługę obrazów JPEG.
Neg: Pokazuje negatywy okien.
Opacify: Zwiększa przezroczystość okien nachodzących na okno nad
    którym aktualnie znajduje się kursor myszy.
Put: Umożliwia ustalenie akcji przesuwających okna na zadane pozycje.
Resizeinfo: Podczas przeskalowywania okna wyświetla informację o
    rozmiarze okna.
Ring: Alternatywny przełącznik aplikacji, który wyświetla okna w
    pierścieniu.
Scaleaddon: Poszerza wtyczkę Scale wyświetlając nazwy okien i
    podświetlając aktualnie wybrane okno.
Shift: Alternatywny przełącznik aplikacji, zapewniający trójwymiarowy
    wygląd procesu przełączania.
Snap: Dodaje przyciąganie podczas przesuwania okien, jeżeli wtyczka
    wobbly jest wyłączona.
Text: Udostępnia wtyczkom renderowanie tekstu za pomocą pango-cairo.
Thumbnail: Wyświetla miniaturki okien gdy mysz najedzie na pozycję na
    pasku zadań.
Vpswitch: Zmienia viewport za pomocą przeprowadzanych na tle akcji
    myszy.
Wall: Ustawia viewporty w ścianę i umożliwia wizualne przesuwanie
    między viewportami, jak również wyświetla okno z podglądem.
Winrules: Umożliwia ustawianie właściwości okien opierając się na
    przypisywaniu po nazwie, typie itp.
Workarounds: Kilka obejść które poprawiają zachowanie starych
    aplikacji.

%package devel
Summary:	Header files for compiz main plugins
Summary(pl.UTF-8):	Pliki nagłówkowe głównych wtyczkek compiza
Group:		X11/Developement/Libraries
Requires:	cairo-devel >= 1.0
Requires:	compiz-devel >= %{vesion}
Requires:	pango-devel >= 1:1.10.0

%description devel
Header files for compiz main plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe głównych wtyczkek compiza.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%{__glib_gettextize}
%{__intltoolize} --automake
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compiz/*.la

%find_lang %{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{pkgname}.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/compiz/*.so
%{_datadir}/compiz/*.xml
%dir %{_datadir}/compiz/filters
%{_datadir}/compiz/Gnome
%{_datadir}/compiz/Oxygen
%{_datadir}/compiz/filters/contrast
%{_datadir}/compiz/filters/grayscale
%{_datadir}/compiz/filters/negative
%{_datadir}/compiz/filters/negative-green
%{_datadir}/compiz/filters/blackandwhite
%{_datadir}/compiz/filters/blueish-filter
%{_datadir}/compiz/filters/deuteranopia
%{_datadir}/compiz/filters/protanopia
%{_datadir}/compiz/filters/sepia
%{_datadir}/compiz/filters/swap-green-blue
%{_datadir}/compiz/filters/swap-red-blue
%{_datadir}/compiz/filters/swap-red-green

%files devel
%defattr(644,root,root,755)
%{_includedir}/compiz/compiz-animation.h
%{_includedir}/compiz/compiz-mousepoll.h
%{_includedir}/compiz/compiz-text.h
%{_pkgconfigdir}/compiz-animation.pc
%{_pkgconfigdir}/compiz-mousepoll.pc
%{_pkgconfigdir}/compiz-text.pc

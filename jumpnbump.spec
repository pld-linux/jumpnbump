# Comment about levels:
# http://jumpnbump.spaceteddy.net/all-levels.tar.gz
# There is archive with 201 levels with never date than
# an archive in our repo (250 files).
Summary:	Multiplayer game
Summary(pl):	Gra dla wielu graczy
Name:		jumpnbump
Version:	1.55
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://www.jumpbump.mine.nu/port/%{name}-%{version}.tar.gz
# Source0-md5:	165873fca1c7164eb08b4875f9e7da07
Source1:	%{name}.desktop
Source2:	%{name}.png
# from http://jumpnbump.spaceteddy.net/
Source3:        %{name}-levels-20020811.tar.bz2
# Source3-md5:  08ebc0f6761ce2dcb560de98808d525d
URL:		http://www.jumpbump.mine.nu/
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc	*.pcx

%description
You're a cute little bunny and you have to avoid the other bunnies
from stomping on you and at the same time try to stomp as many
opponents as possible. Jump & Bump is multiplayer only with up to four
players simultaneously. Gather the local crew and have a blast.

%description -l pl
W tej grze gracz jest ma³ym królikiem, który musi unikn±æ rozdeptania
przez inne króliki, a jednocze¶nie próbowaæ rozdeptaæ jak najwiêcej
przeciwników. Jump & Bump to gra wy³±cznie dla wielu graczy -
maksymalnie czterech naraz. Zgromad¼ w³asn± dru¿ynê i baw siê dobrze.

%package levelpack
Summary:	Additional levels for Jump & Bump
Summary(pl):	Dodatkowe poziomy dla Jump & Bump
Group:		Applications/Games
Requires:	%{name} = %{version}-%{release}

%description levelpack
249 additional levels for Jump & Bump.

%description levelpack -l pl
249 dodatkowych poziomów dla Jump & Bump.

%prep
%setup -q -n %{name}-1.50
# Archiwe has wrong directory name, that why there is -n switch

%build
%configure

cat Makefile | sed "s/-o root -g [^ ]\+//g" > Makefile-
mv -f Makefile- Makefile

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{!?debug:-DNDEBUG} -DUSE_SDL -DUSE_NET \
		-I%{_builddir}/%{name}-%{version} \
		`sdl-config --cflags` \
		-Dstricmp=strcasecmp -Dstrnicmp=strncasecmp" \
	LFLAGS="%{rpmldflags}" \
	PREFIX="%{_prefix}"


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man6,%{_desktopdir},%{_pixmapsdir},%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# rm $RPM_BUILD_ROOT%{_bindir}/*.{fbcon,svgalib}
# If You are sure to uncomment the line aboce, do it.

install %{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
tar jxvf %{SOURCE3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LINKS README TODO readme.txt source.txt
%doc levelmaking
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/jumpbump.dat
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop

%files levelpack
%defattr(644,root,root,755)
%{_datadir}/%{name}/*.dat

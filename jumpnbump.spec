Summary:	Multiplayer game
Summary(pl):	Gra dla wielu graczy
Name:		jumpnbump
Version:	1.35
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://www.jumpbump.mine.nu/port/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://www.jumpbump.mine.nu/
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You're a cute little bunny and you have to avoid the other bunnies
from stomping on you and at the same time try to stomp as many
opponents as possible. Jump & bump is multiplayer only with up to four
players simultaneously. Gather the local crew and have a blast.

%prep
%setup -q

cat Makefile | sed "s/-o root -g games//g" > Makefile-
mv -f Makefile- Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DUSE_SDL -DNDEBUG -I. `sdl-config --cflags` -Dstricmp=strcasecmp -Dstrnicmp=strncasecmp" \
	LFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man6,%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm $RPM_BUILD_ROOT%{_prefix}/games/%{name}.{fbcon,svgalib}

install %{name}.6 $RPM_BUILD_ROOT%{_mandir}/man6

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LINKS README TODO readme.txt source.txt
%attr(755,root,root) %{_prefix}/games/*
%{_datadir}/%{name}
%{_mandir}/man6/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/Arcade/*

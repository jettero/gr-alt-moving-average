
########################################################################
# Install GRC xml files
########################################################################

list(APPEND grc_sources
    wmoving.xml
)

install(
    FILES ${grc_sources}
    DESTINATION ${GRC_BLOCKS_DIR}
    COMPONENT "gr_alt_moving_average_python"
)

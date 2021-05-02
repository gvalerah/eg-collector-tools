
@main.route('/collector/faq', methods=['GET'])
def collector_faq():
    logger.warning('collector_faq(): IN')
    try:
        logger.warning(f'collector_faq(): current_user = {current_user}')        
    except Exception as e:
        logger.error(f"collector_faq(): exception: {str(e)}")
    
    return render_template('collector_faq.html')
    
@main.route('/collector/about', methods=['GET'])
def collector_about():
    logger.warning('collector_about(): IN')
    try:
        logger.warning(f'collector_about(): current_user = {current_user}')        
    except Exception as e:
        logger.error(f"collector_about(): exception: {str(e)}")
    
    return render_template('collector_about.html')
